# Agrione - Nông nghiệp cây mía (`frm_sugar_sales`)

Giải pháp **nông nghiệp cây mía** của Agrione trên nền **Odoo 19.0**. Module **miễn phí**
này là phần **kế hoạch giao mía nguyên liệu về nhà máy nhiều đợt** trong vụ — một mắt xích
của hệ sinh thái ERP cây mía Agrione.

[![License: LGPL-3](https://img.shields.io/badge/license-LGPL--3-blue.svg)](LICENSE)
![Odoo 19.0](https://img.shields.io/badge/Odoo-19.0-714B67.svg)

## Hệ sinh thái ERP cây mía Agrione

Mua hàng · Kho (vật tư nông nghiệp / vật liệu sản xuất / thành phẩm) · Bán hàng ·
Nhân sự · Kế toán · Canh tác & thu hoạch. Bộ giải pháp đầy đủ triển khai theo yêu cầu —
liên hệ [agrione.vn](https://agrione.vn).

## Module miễn phí này gồm

- **Kế hoạch giao theo đợt** — mỗi đơn thêm nhiều đợt giao (sản phẩm · số lượng · ngày); vụ mía giao làm nhiều chuyến trong nhiều tuần.
- **Sinh phiếu kho tự động** — mỗi đợt tạo phiếu xuất kho thật, đúng số lượng & ngày.
- **Theo dõi tiến độ** — đã giao / còn lại / % hoàn tất theo phiếu kho thực tế.

## Cài đặt

```bash
odoo -i frm_sugar_sales -d <database>
```

Chỉ phụ thuộc `sale_management` + `stock` (chuẩn Odoo) — cài độc lập, dùng ngay.

## Kỹ thuật

| | |
|---|---|
| Phiên bản Odoo | 19.0 (Community & Enterprise) |
| Phụ thuộc | `sale_management`, `stock` |
| Giấy phép | LGPL-3 |
| Model chính | `frm.sale.delivery.schedule`, mở rộng `sale.order` |

## Giấy phép

LGPL-3 — xem [LICENSE](LICENSE).

---

Phát triển bởi **BSD** · [agrione.vn](https://agrione.vn) · [bsdinsight.com](https://bsdinsight.com)
