# -*- coding: utf-8 -*-
{
    'name': 'Agrione – Bán hàng & Kế hoạch giao hàng',
    'version': '19.0.2.0.0',
    'summary': 'Đơn hàng lớn giao nhiều đợt: mỗi đơn có kế hoạch giao (ngày + số '
               'lượng từng đợt), mỗi đợt sinh phiếu giao thật + theo dõi đã giao / '
               'còn lại. Module ĐỘC LẬP — chỉ cần Sale + Stock.',
    'description': """
Agrione – Bán hàng & Kế hoạch giao hàng
=======================================
Module **độc lập** (chỉ phụ thuộc Sale + Stock của Odoo) cho bài toán bán hàng
đơn lớn nhưng **giao nhiều đợt** — điển hình ngành đường (bán 1.000 tấn nhưng
giao làm nhiều chuyến trong nhiều tuần).

* **Kế hoạch giao hàng trên từng đơn** — thêm các đợt giao (sản phẩm · số lượng
  · ngày hẹn) ngay trong tab của đơn bán hàng.
* **Sinh phiếu giao thật cho từng đợt** — bấm *Tạo phiếu giao* → phiếu xuất kho
  → khách, đúng số lượng & ngày; hoặc *Tạo tất cả phiếu giao* một lần.
* **Theo dõi tiến độ** — đã giao / còn lại / % hoàn tất, cập nhật theo phiếu kho
  thực tế; mỗi đợt có trạng thái Chờ tạo phiếu / Đã tạo phiếu / Giao một phần /
  Đã giao đủ.

Không phụ thuộc module nào khác của Agrione — dùng chung nền Odoo Community.
""",
    'category': 'Sales',
    'author': 'Agrione (BSD)',
    'license': 'LGPL-3',
    'website': 'https://agrione.vn',
    'maintainer': 'Agrione (BSD)',
    'images': ['static/description/cover.png'],
    'depends': ['sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/delivery_schedule_views.xml',
        'views/sale_order_views.xml',
        'views/menu_views.xml',
        'reports/sale_contract_report.xml',
        'reports/delivery_note_report.xml',
    ],
    'demo': [
        'demo/demo_sugar_sales.xml',
    ],
    'installable': True,
    'application': False,
}
