# Database

Database sử dụng MySQL 8 và UTF-8 (`utf8mb4`). File [`database/schema.sql`](../database/schema.sql) là khung khởi tạo ban đầu; [`database/seed.sql`](../database/seed.sql) chỉ chứa dữ liệu mẫu placeholder.

Thông tin kết nối được đọc từ biến môi trường hoặc file `server/.env`, không lưu mật khẩu thật trong Git.
