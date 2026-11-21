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
- **Server:** Ứng dụng Python sử dụng FastAPI, tiếp nhận và xử lý yêu cầu từ Client.
- **Database:** MySQL lưu trữ dữ liệu tập trung.
- **Giao tiếp:** Client gửi HTTP Request đến Server và nhận kết quả JSON.
- **Bảo mật:** Client không kết nối trực tiếp đến MySQL. Việc xác thực và phân quyền được thực hiện tại Server.

## 4. Phân công công việc nhóm

| Thành viên | Module phụ trách | Công việc chính |
|---|---|---|
| Thành viên 1 | Kiến trúc Client–Server và quản lý hệ thống | Thiết kế MVC, xây dựng Server nền tảng, kết nối MySQL, API dùng chung, đăng nhập, phân quyền, quản lý tài khoản và nhân viên |
| Thành viên 2 | Quản lý khách hàng, thiết bị và dịch vụ | Khách hàng vãng lai, thành viên, tổ chức, người đại diện, địa điểm, thiết bị điều hòa và danh mục dịch vụ |
| Thành viên 3 | Tiếp nhận yêu cầu và phân công kỹ thuật | Tiếp nhận yêu cầu, xác nhận lịch hẹn, quản lý trạng thái, phân công kỹ thuật viên |
| Thành viên 4 | Thực hiện kỹ thuật và lịch sử dịch vụ | Quản lý công việc được giao, cập nhật tiến độ, tình trạng thiết bị, kết quả sửa chữa, vật tư và lịch sử dịch vụ |
| Thành viên 5 | Hóa đơn, thanh toán và báo cáo | Lập hóa đơn, chi tiết hóa đơn, xác nhận thanh toán, thống kê doanh thu và báo cáo hoạt động |

**Nguyên tắc phân công:** Mỗi thành viên phụ trách module của mình, bao gồm giao diện PySide6, Backend/API, Controller, Model và xử lý dữ liệu. Thành viên 1 phụ trách nền tảng Client–Server chung.

## 5. Công việc chung

- Cùng thống nhất yêu cầu nghiệp vụ và thiết kế cơ sở dữ liệu tổng thể.
- Thống nhất cấu trúc API và quy tắc trao đổi dữ liệu.
- Từng thành viên phát triển module theo phân công.
- Tích hợp các module vào Server và Client chung.
- Cả nhóm cùng kiểm thử, sửa lỗi và hoàn thiện sản phẩm.
- Cùng xây dựng báo cáo, slide và chuẩn bị thuyết trình.

## 6. Cấu trúc mã nguồn

```text
Dich_vu_dien_lanh/
├── client/
│   ├── models/
│   ├── views/
│   ├── controllers/
│   ├── api/
│   └── main.py
│
├── server/
│   ├── app/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── routers/
│   │   ├── database/
│   │   ├── core/
│   │   └── main.py
│   └── requirements.txt
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── docs/
│   ├── architecture.md
│   ├── database.md
│   └── task_assignment.md
│
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

## 8. Cài đặt môi trường

Mở Terminal tại thư mục gốc dự án.

Tạo môi trường ảo:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Cài đặt thư viện Server:

```powershell
pip install -r server/requirements.txt
```

Cài đặt thư viện Client:

```powershell
pip install PySide6 httpx
```

Tạo file cấu hình môi trường từ `.env.example`:

```powershell
Copy-Item server/.env.example server/.env
```

Cấu hình thông tin kết nối MySQL trong file `server/.env`.

Tạo cơ sở dữ liệu bằng MySQL Workbench hoặc MySQL CLI:

```sql
SOURCE database/schema.sql;
SOURCE database/seed.sql;
```

## 9. Hướng dẫn chạy chương trình

**Chạy Server:**

Từ thư mục gốc dự án:

```powershell
$env:PYTHONPATH = "server"
uvicorn app.main:app --reload --app-dir server
```

**Chạy Client:**

Mở một Terminal khác:

```powershell
python client/main.py
```

Server mặc định chạy tại:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/health
- http://127.0.0.1:8000/docs

## 10. Quản lý tiến độ

Các thành viên cập nhật trạng thái công việc thông qua GitHub Issues hoặc Projects:

- `Todo`: Chưa thực hiện.
- `In Progress`: Đang thực hiện.
- `Review`: Chờ xem xét và tích hợp.
- `Done`: Hoàn thành.

**Lưu ý:** Phân công trên thể hiện trách nhiệm chính của từng thành viên; việc tích hợp, kiểm thử và hoàn thiện sản phẩm là trách nhiệm chung của cả nhóm.