# -*- coding: utf-8 -*-
"""Kế hoạch giao hàng theo đợt — module ĐỘC LẬP (chỉ Sale + Stock).

Mỗi đơn hàng có nhiều "đợt giao" (frm.sale.delivery.schedule): sản phẩm + số
lượng + ngày hẹn. Mỗi đợt sinh một phiếu xuất kho (stock.picking) → khách, và
theo dõi đã giao / còn lại theo phiếu kho thực tế.
"""
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleDeliverySchedule(models.Model):
    _name = 'frm.sale.delivery.schedule'
    _description = 'Đợt giao hàng theo kế hoạch'
    _order = 'order_id, planned_date, sequence, id'

    order_id = fields.Many2one(
        'sale.order', string='Đơn hàng', required=True,
        ondelete='cascade', index=True, copy=False)
    sequence = fields.Integer(string='Thứ tự', default=10)
    partner_id = fields.Many2one(related='order_id.partner_id', string='Khách hàng', store=True)
    company_id = fields.Many2one(related='order_id.company_id', store=True)
    currency_id = fields.Many2one(related='order_id.currency_id')

    product_id = fields.Many2one(
        'product.product', string='Sản phẩm', required=True,
        domain="[('sale_ok', '=', True)]")
    product_uom_id = fields.Many2one('uom.uom', string='ĐVT')
    planned_qty = fields.Float(string='SL theo kế hoạch', required=True)
    planned_date = fields.Date(string='Ngày giao dự kiến', required=True)
    note = fields.Char(string='Ghi chú')

    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Kho xuất',
        help='Để trống → tự lấy kho của đơn hàng, hoặc kho thành phẩm (mã TP), '
             'hoặc kho đầu tiên của công ty.')

    picking_id = fields.Many2one('stock.picking', string='Phiếu giao', readonly=True, copy=False)
    picking_state = fields.Selection(related='picking_id.state', string='TT phiếu', readonly=True)
    qty_delivered = fields.Float(string='Đã giao', compute='_compute_qty_delivered', store=True)
    delivery_state = fields.Selection([
        ('pending', 'Chờ tạo phiếu'),
        ('scheduled', 'Đã tạo phiếu'),
        ('partial', 'Giao một phần'),
        ('done', 'Đã giao đủ'),
    ], string='Tình trạng', compute='_compute_delivery_state', store=True, default='pending')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id and not self.product_uom_id:
            self.product_uom_id = self.product_id.uom_id

    @api.depends('picking_id.state', 'picking_id.move_ids.quantity', 'picking_id.move_ids.state')
    def _compute_qty_delivered(self):
        for rec in self:
            qty = 0.0
            pk = rec.picking_id
            if pk and pk.state == 'done':
                qty = sum(pk.move_ids.filtered(lambda m: m.state == 'done').mapped('quantity'))
            rec.qty_delivered = qty

    @api.depends('picking_id', 'picking_id.state', 'qty_delivered', 'planned_qty')
    def _compute_delivery_state(self):
        for rec in self:
            if not rec.picking_id:
                rec.delivery_state = 'pending'
            elif rec.picking_id.state != 'done':
                rec.delivery_state = 'scheduled'
            elif rec.qty_delivered + 1e-6 >= rec.planned_qty:
                rec.delivery_state = 'done'
            else:
                rec.delivery_state = 'partial'

    def _delivery_locations(self):
        """(picking_type, source_location, customer_location) — không cần module khác."""
        self.ensure_one()
        Wh = self.env['stock.warehouse']
        company = self.company_id or self.env.company
        # Ưu tiên: kho chỉ định trên đợt → kho thành phẩm (mã TP) → kho của đơn → kho đầu tiên
        wh = self.warehouse_id
        if not wh:
            wh = Wh.search([('code', '=', 'TP'), ('company_id', '=', company.id)], limit=1)
        if not wh and 'warehouse_id' in self.order_id._fields:
            wh = self.order_id.warehouse_id
        if not wh:
            wh = Wh.search([('company_id', '=', company.id)], limit=1)
        if not wh:
            raise UserError(_('Chưa có kho nào để xuất giao — kiểm tra cấu hình kho.'))
        ptype = wh.out_type_id
        if not ptype:
            raise UserError(_('Kho "%s" chưa có kiểu phiếu xuất (Delivery).') % wh.display_name)
        src = ptype.default_location_src_id or wh.lot_stock_id
        dest = self.env.ref('stock.stock_location_customers', raise_if_not_found=False)
        if not dest:
            raise UserError(_('Thiếu địa điểm Khách hàng của hệ thống.'))
        return ptype, src, dest

    def action_generate_delivery(self):
        """Sinh phiếu xuất kho cho từng đợt giao."""
        Picking = self.env['stock.picking']
        for rec in self:
            if rec.picking_id:
                continue
            if rec.planned_qty <= 0:
                raise UserError(_('Đợt giao chưa có số lượng.'))
            product = rec.product_id
            if not product.is_storable:
                raise UserError(_(
                    'Sản phẩm "%s" chưa phải loại lưu kho (Hàng tồn kho) nên không '
                    'xuất giao được. Mở sản phẩm → đặt Loại = "Hàng tồn kho".'
                ) % product.display_name)
            ptype, src, dest = rec._delivery_locations()
            uom = rec.product_uom_id or product.uom_id
            picking = Picking.create({
                'picking_type_id': ptype.id,
                'partner_id': rec.partner_id.id,
                'origin': rec.order_id.name,
                'scheduled_date': rec.planned_date,
                'location_id': src.id,
                'location_dest_id': dest.id,
                'move_ids': [(0, 0, {
                    'description_picking': '%s — giao %s' % (product.display_name, rec.planned_date or ''),
                    'product_id': product.id,
                    'product_uom': uom.id,
                    'product_uom_qty': rec.planned_qty,
                    'location_id': src.id,
                    'location_dest_id': dest.id,
                })],
            })
            picking.action_confirm()
            picking.action_assign()
            rec.picking_id = picking.id
        return True

    def action_open_picking(self):
        self.ensure_one()
        if not self.picking_id:
            raise UserError(_('Đợt giao này chưa có phiếu giao.'))
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'stock.picking',
            'res_id': self.picking_id.id,
            'view_mode': 'form',
        }
