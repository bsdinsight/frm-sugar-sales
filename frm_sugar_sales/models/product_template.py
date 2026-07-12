# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_finished_good = fields.Boolean(
        string='Thành phẩm bán ra',
        help='Đánh dấu sản phẩm là THÀNH PHẨM của nhà máy (đường, mật rỉ, bã mía, '
             'bùn lọc…) — chỉ những sản phẩm này hiện trong danh mục Sản phẩm của '
             'app Bán hàng. Vật tư nông nghiệp / dịch vụ / công lao động KHÔNG tick.',
        index=True,
    )
