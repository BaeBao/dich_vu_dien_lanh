"""Điểm khởi chạy Server FastAPI."""

from fastapi import FastAPI

from app.routers.health import router as health_router

app = FastAPI(
    title="Air Conditioning Service Management API",
    version="0.1.0",
    description="API nền tảng cho hệ thống quản lý dịch vụ điện lạnh tại Đà Nẵng.",
)
app.include_router(health_router, prefix="/api")


@app.get("/", tags=["system"])
def read_root() -> dict[str, str]:
    """Trả về thông tin cơ bản để kiểm tra Server đã khởi động."""
    return {"message": "Air Conditioning Service Management API", "status": "running"}
