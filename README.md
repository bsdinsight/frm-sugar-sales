# Agrione – Bán hàng & Kế hoạch giao hàng nhiều đợt (`frm_sugar_sales`)

Module Odoo **19.0** cho bài toán bán **đơn hàng lớn nhưng giao làm nhiều đợt** —
điển hình ngành đường, nông sản, vật liệu, phân bón (bán 1.000 tấn, giao rải nhiều
chuyến trong nhiều tuần).

[![License: LGPL-3](https://img.shields.io/badge/license-LGPL--3-blue.svg)](LICENSE)
![Odoo 19.0](https://img.shields.io/badge/Odoo-19.0-714B67.svg)

## Tính năng

- **Kế hoạch giao theo đợt** — thêm các đợt giao (sản phẩm · số lượng · ngày hẹn) ngay trong một tab của đơn bán hàng.
- **Sinh phiếu giao thật** — *Tạo phiếu giao* → phiếu xuất kho đúng số lượng & ngày; hoặc *Tạo tất cả* một lần.
- **Theo dõi tiến độ** — đã giao / còn lại / % hoàn tất, cập nhật theo phiếu kho thực tế.
- **Trạng thái từng đợt** — Chờ tạo phiếu → Đã tạo phiếu → Giao một phần → Đã giao đủ.
- **Mẫu in** — Hợp đồng bán hàng & Phiếu giao hàng (tiếng Việt).

## Cài đặt

```bash
odoo -i frm_sugar_sales -d <database>
```

**Module độc lập** — chỉ phụ thuộc `sale_management` + `stock` (chuẩn Odoo), không cần module ngoài nào.

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

Phát triển bởi **Agrione (BSD)** · [agrione.vn](https://agrione.vn) · [bsdinsight.com](https://bsdinsight.com)
