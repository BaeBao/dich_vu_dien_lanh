"""HTTP client dùng chung cho Client; Client không truy cập MySQL trực tiếp."""

from typing import Any

import httpx


class ApiClient:
    """Client REST tối giản để các controller tái sử dụng."""

    def __init__(self, base_url: str = "http://127.0.0.1:8000/api", timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str) -> dict[str, Any]:
        """Gửi GET request và trả về JSON object."""
        response = httpx.get(f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout)
        response.raise_for_status()
        return response.json()
