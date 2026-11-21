"""Router kiểm tra trạng thái hoạt động của Server."""

from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Endpoint không phụ thuộc Database, dùng để kiểm tra nhanh."""
    return {"status": "ok"}
