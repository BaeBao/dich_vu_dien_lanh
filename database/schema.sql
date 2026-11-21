-- Khung Database ban đầu. Nghiệp vụ chi tiết sẽ được bổ sung sau.
CREATE DATABASE IF NOT EXISTS air_conditioning_system
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE air_conditioning_system;

-- Bảng người dùng tối thiểu để dành chỗ cho module xác thực.
CREATE TABLE IF NOT EXISTS users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'staff',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
