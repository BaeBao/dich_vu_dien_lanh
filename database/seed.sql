-- Dữ liệu mẫu khung. Mật khẩu dưới đây chỉ là placeholder, không dùng production.
USE air_conditioning_system;

INSERT INTO users (username, password_hash, role)
VALUES ('admin', 'REPLACE_WITH_HASH', 'admin')
ON DUPLICATE KEY UPDATE username = username;
