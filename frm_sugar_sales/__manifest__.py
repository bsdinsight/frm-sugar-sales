# -*- coding: utf-8 -*-
{
    'name': 'Agrione - Nông nghiệp cây mía',
    'version': '19.0.2.5.0',
    'summary': 'Nông nghiệp cây mía Agrione — module miễn phí lập kế hoạch giao mía '
               'nguyên liệu về nhà máy nhiều đợt trong vụ (nền Sale + Stock). Thuộc hệ '
               'sinh thái ERP mía: mua hàng, kho (vật tư nông nghiệp / vật liệu sản xuất '
               '/ thành phẩm), bán hàng, nhân sự, kế toán.',
    'description': """
Agrione - Nông nghiệp cây mía
=============================
Giải pháp **nông nghiệp cây mía toàn diện** của Agrione trên nền Odoo — từ vùng
nguyên liệu đến nhà máy.

Chức năng nông nghiệp cây mía
-----------------------------
* **Vùng nguyên liệu & thửa đất** — nông trường/lô/khu, thửa nông dân vệ tinh, mã vùng trồng, giống & năm gốc (mía tơ · gốc 1 · gốc 2…).
* **Canh tác & nhật ký đồng ruộng** — quy trình theo giống + năm gốc, giao việc cán bộ nông vụ theo ngày, thăm vườn ghi sâu bệnh/dinh dưỡng/độ chín.
* **Đầu tư & bao tiêu nông dân vệ tinh** — khế ước đầu tư, giải ngân nhiều đợt, cấn trừ vào tiền mía.
* **Thu hoạch & giao mía** — lịch đốn theo độ chín, đội đốn/công đốn, cổng cân (đo chữ đường CCS), giao nhiều đợt về nhà máy.
* **Truy xuất & chất lượng** — lịch sử canh tác–đầu tư–thu hoạch theo thửa, CCS/tạp chất theo lô.
* **Ứng dụng di động 3 vai** — nông dân · cán bộ nông vụ · tài xế, hoạt động offline.

Module miễn phí này gồm
-----------------------
* **Kế hoạch giao theo đợt** — chốt sản lượng, chia lịch giao theo tiến độ đốn & độ chín; giao mía nguyên liệu về nhà máy nhiều đợt trong vụ ép.
* **Sinh phiếu giao thật cho từng đợt** — tạo phiếu xuất kho đúng số lượng & ngày.
* **Theo dõi tiến độ** — đã giao / còn lại / % hoàn tất theo phiếu kho thực tế.

Chỉ phụ thuộc Sale + Stock của Odoo — cài độc lập, dùng ngay.

Kèm hệ sinh thái vận hành: Mua hàng · Kho (vật tư nông nghiệp / vật liệu sản xuất / thành phẩm) · Bán hàng · Nhân sự · Kế toán.
""",
    'category': 'Sales',
    'author': 'BSD',
    'license': 'LGPL-3',
    'website': 'https://agrione.vn',
    'maintainer': 'BSD',
    'images': [
        'static/description/cover.png',
        'static/description/screenshot_1_map.png',
        'static/description/screenshot_3_cultivation.png',
        'static/description/screenshot_2_plots.png',
        'static/description/screenshot_4_harvest.png',
        'static/description/screenshot_5_investment.png',
    ],
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
