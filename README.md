# HỆ THỐNG QUẢN LÝ DỊCH VỤ ĐIỆN LẠNH ĐÀ NẴNG

## 1. Giới thiệu dự án

**Tên đề tài:** Xây dựng hệ thống quản lý dịch vụ điện lạnh tại trung tâm thành phố Đà Nẵng.

**Mục tiêu:** Xây dựng ứng dụng hỗ trợ quản lý hoạt động kinh doanh dịch vụ điện lạnh, từ tiếp nhận yêu cầu, đặt lịch, phân công kỹ thuật viên, thực hiện sửa chữa, lập hóa đơn đến thanh toán và thống kê báo cáo.

## 2. Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ lập trình | Python |
| Giao diện Desktop Client | PySide6 |
| Backend Server | FastAPI |
| Cơ sở dữ liệu | MySQL 8.x |
| ORM | SQLAlchemy |
| Giao tiếp mạng | REST API – HTTP/TCP/IP |
| Định dạng trao đổi | JSON |
| Kiến trúc mã nguồn | MVC |
| Quản lý mã nguồn | GitHub |

## 3. Kiến trúc hệ thống

Hệ thống được xây dựng theo mô hình Client–Server kết hợp kiến trúc MVC.

- **Client:** Ứng dụng Desktop Python sử dụng PySide6, tổ chức theo Model – View – Controller.
- **Server:** Ứng dụng Python sử dụng FastAPI, tiếp nhận và xử lý yêu cầu từ các Client.
- **Database:** MySQL lưu trữ dữ liệu tập trung.
- **Giao tiếp:** Client gửi HTTP Request đến Server và nhận kết quả JSON.
- **Bảo mật:** Client không kết nối trực tiếp đến MySQL. Việc xác thực và phân quyền được thực hiện tại Server.

## 4. Phân công công việc nhóm

| Thành viên | Module phụ trách | Công việc chính |
|---|---|---|
| Thành viên 1 | Kiến trúc Client–Server và quản lý hệ thống | Thiết kế MVC, xây dựng Server độc lập, kết nối MySQL, API dùng chung, đăng nhập, đăng xuất, phân quyền, quản lý tài khoản và nhân viên |
| Thành viên 2 | Quản lý khách hàng, thiết bị và dịch vụ | Khách hàng vãng lai, thành viên, tổ chức, người đại diện, địa điểm, thiết bị điều hòa, danh mục dịch vụ |
| Thành viên 3 | Tiếp nhận yêu cầu và phân công kỹ thuật | Tiếp nhận yêu cầu, xác nhận lịch hẹn, quản lý trạng thái, trưởng kỹ thuật phân công kỹ thuật viên |
| Thành viên 4 | Thực hiện kỹ thuật và lịch sử dịch vụ | Quản lý công việc được giao, cập nhật tiến độ, tình trạng thiết bị, kết quả sửa chữa, vật tư và lịch sử dịch vụ |
| Thành viên 5 | Hóa đơn, thanh toán và báo cáo | Lập hóa đơn, chi tiết hóa đơn, xác nhận thanh toán, thống kê doanh thu và báo cáo hoạt động |

**Nguyên tắc phân công:** Mỗi thành viên phụ trách trọn vẹn module của mình, bao gồm giao diện PySide6, Backend/API, Controller, Model và xử lý dữ liệu MySQL.

## 5. Công việc chung

- Cùng thống nhất yêu cầu nghiệp vụ và thiết kế cơ sở dữ liệu tổng thể.
- Thống nhất cấu trúc API và quy tắc trao đổi dữ liệu.
- Từng thành viên phát triển module theo phân công.
- Tích hợp các module vào Server và Client chung.
- Cả nhóm cùng kiểm thử, sửa lỗi và hoàn thiện sản phẩm.
- Cùng xây dựng báo cáo, slide và chuẩn bị thuyết trình.

## 6. Cấu trúc mã nguồn dự kiến

```text
AIR_CONDITIONING_SYSTEM/
├── client/
│   ├── models/
│   ├── views/
│   ├── controllers/
│   ├── api/
│   └── main.py
│
├── server/
│   ├── models/
│   ├── schemas/
│   ├── controllers/
│   ├── services/
│   ├── routers/
│   ├── database/
│   ├── core/
│   └── main.py
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── docs/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 7. Quy định phối hợp và tích hợp

1. Thành viên 1 chịu trách nhiệm duy trì cấu trúc Server, Client và quy chuẩn API chung.
2. Các thành viên phát triển module độc lập theo cấu trúc MVC đã thống nhất.
3. Các module sử dụng chung kết nối Database và cơ chế xác thực.
4. Không để Client kết nối trực tiếp đến MySQL.
5. Mọi thay đổi liên quan đến bảng dữ liệu hoặc API dùng chung phải được trao đổi trước khi cập nhật.
6. Mã nguồn được cập nhật thường xuyên lên GitHub theo từng module.

## 8. Tiến độ và trạng thái thực hiện

Các thành viên cập nhật trạng thái công việc thông qua GitHub Issues hoặc Projects:

- `Todo`: Chưa thực hiện.
- `In Progress`: Đang thực hiện.
- `Review`: Chờ xem xét và tích hợp.
- `Done`: Hoàn thành.

**Lưu ý:** Phân công trên thể hiện trách nhiệm chính của từng thành viên; việc tích hợp, kiểm thử và hoàn thiện sản phẩm là trách nhiệm chung của cả nhóm.
