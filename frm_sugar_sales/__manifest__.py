# -*- coding: utf-8 -*-
{
    'name': 'Agrione - Nông nghiệp cây mía',
    'version': '19.0.2.1.0',
    'summary': 'Nông nghiệp cây mía Agrione — module miễn phí lập kế hoạch giao mía '
               'nguyên liệu về nhà máy nhiều đợt trong vụ (nền Sale + Stock). Thuộc hệ '
               'sinh thái ERP mía: mua hàng, kho (vật tư nông nghiệp / vật liệu sản xuất '
               '/ thành phẩm), bán hàng, nhân sự, kế toán.',
    'description': """
Agrione - Nông nghiệp cây mía
=============================
Giải pháp **nông nghiệp cây mía** của Agrione trên nền Odoo. Module miễn phí này là
phần **kế hoạch giao mía nguyên liệu về nhà máy nhiều đợt** trong vụ thu hoạch —
một mắt xích của hệ sinh thái ERP mía Agrione.

Hệ sinh thái ERP mía Agrione
----------------------------
* **Mua hàng** — vật tư nông nghiệp (giống, phân, thuốc) và nguyên vật liệu sản xuất.
* **Kho** — vật tư nông nghiệp · vật liệu sản xuất · thành phẩm (đường).
* **Bán hàng** — giao mía nguyên liệu / thành phẩm nhiều đợt theo vụ.
* **Nhân sự** — chấm công, khoán việc nông trường.
* **Kế toán** — hạch toán mùa vụ, giá thành.

Module miễn phí này gồm
-----------------------
* **Kế hoạch giao theo đợt** — thêm các đợt giao (sản phẩm · số lượng · ngày) ngay
  trên đơn; điển hình vụ mía: giao mía về nhà máy làm nhiều chuyến trong nhiều tuần.
* **Sinh phiếu giao thật cho từng đợt** — tạo phiếu xuất kho đúng số lượng & ngày.
* **Theo dõi tiến độ** — đã giao / còn lại / % hoàn tất theo phiếu kho thực tế.

Chỉ phụ thuộc Sale + Stock của Odoo — cài độc lập, dùng ngay.
""",
    'category': 'Sales',
    'author': 'BSD',
    'license': 'LGPL-3',
    'website': 'https://agrione.vn',
    'maintainer': 'BSD',
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
