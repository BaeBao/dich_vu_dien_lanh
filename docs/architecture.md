# Kiến trúc hệ thống

Hệ thống dùng mô hình Client–Server kết hợp MVC. Client PySide6 chỉ gọi REST API qua HTTP/JSON; Server FastAPI là lớp duy nhất truy cập MySQL thông qua SQLAlchemy.

## Luồng chính

`Client View -> Client Controller -> API Client -> FastAPI Router -> Controller -> Service -> SQLAlchemy Model -> MySQL`

Các module nghiệp vụ được phát triển độc lập theo phân công, sau đó tích hợp qua router, service và giao diện chung.
