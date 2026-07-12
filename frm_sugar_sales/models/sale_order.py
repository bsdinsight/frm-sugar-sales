# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_schedule_line_ids = fields.One2many(
        'frm.sale.delivery.schedule', 'order_id',
        string='Kế hoạch giao hàng', copy=True)
    delivery_schedule_count = fields.Integer(compute='_compute_delivery_schedule')
    scheduled_qty = fields.Float(string='SL theo kế hoạch', compute='_compute_delivery_schedule')
    delivered_qty = fields.Float(string='Đã giao', compute='_compute_delivery_schedule')
    delivery_progress_pct = fields.Float(string='% đã giao', compute='_compute_delivery_schedule')

    @api.depends('delivery_schedule_line_ids.planned_qty',
                 'delivery_schedule_line_ids.qty_delivered')
    def _compute_delivery_schedule(self):
        for order in self:
            lines = order.delivery_schedule_line_ids
            planned = sum(lines.mapped('planned_qty'))
            delivered = sum(lines.mapped('qty_delivered'))
            order.delivery_schedule_count = len(lines)
            order.scheduled_qty = planned
            order.delivered_qty = delivered
            order.delivery_progress_pct = (delivered / planned * 100.0) if planned else 0.0

    def action_generate_all_deliveries(self):
        self.ensure_one()
        pending = self.delivery_schedule_line_ids.filtered(lambda l: not l.picking_id)
        if not pending:
            raise UserError(_('Mọi đợt trong kế hoạch đã có phiếu giao.'))
        pending.action_generate_delivery()
        return self.action_view_delivery_pickings()

    def action_view_delivery_pickings(self):
        self.ensure_one()
        pickings = self.delivery_schedule_line_ids.mapped('picking_id')
        return {
            'type': 'ir.actions.act_window',
            'name': _('Phiếu giao — %s') % self.name,
            'res_model': 'stock.picking',
            'view_mode': 'list,form',
            'domain': [('id', 'in', pickings.ids)],
            'context': {'create': False},
        }
