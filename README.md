# Hệ thống quản lý dịch vụ điện lạnh

Dự án đại học xây dựng hệ thống quản lý dịch vụ điện lạnh tại trung tâm thành phố Đà Nẵng.

## Công nghệ

- Python, PySide6 cho Client.
- FastAPI, SQLAlchemy và MySQL 8 cho Server.
- REST API, HTTP và JSON cho giao tiếp Client–Server.
- Kiến trúc Client–Server kết hợp MVC.

## Nguyên tắc kiến trúc

Client tổ chức theo Models, Views, Controllers và API. Server tổ chức theo Models (SQLAlchemy), Schemas (Pydantic), Controllers, Services, Routers, Database và Core. Client không kết nối trực tiếp tới MySQL.

## Cài đặt nhanh

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r server\requirements.txt
pip install PySide6 httpx
Copy-Item server\.env.example server\.env
```

Tạo Database bằng MySQL Workbench hoặc MySQL CLI:

```sql
SOURCE database/schema.sql;
SOURCE database/seed.sql;
```

## Chạy

Từ thư mục gốc, với môi trường ảo đã kích hoạt:

```powershell
$env:PYTHONPATH = "server"
uvicorn app.main:app --reload --app-dir server
```

Client chạy ở terminal khác:

```powershell
python client\main.py
```

Server có thể kiểm tra tại `http://127.0.0.1:8000/` và `http://127.0.0.1:8000/api/health`.

## Đưa lên GitHub

1. Tạo repository mới trên GitHub.
2. Kiểm tra `.gitignore`, đặc biệt không commit file `server/.env`.
3. Chạy `git init`, `git add .`, `git commit -m "Initialize project structure"`.
4. Thêm remote GitHub và chạy `git push -u origin main`.

Phân công chi tiết xem tại [`docs/task_assignment.md`](docs/task_assignment.md).
