"""Đọc cấu hình Server từ biến môi trường hoặc file .env."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Cấu hình tối thiểu cho giai đoạn khởi tạo dự án."""

    app_name: str = "Air Conditioning Service Management API"
    debug: bool = False
    mysql_user: str = "root"
    mysql_password: str = "change_me"
    mysql_host: str = "localhost"
    mysql_port: int = 3306
    mysql_database: str = "air_conditioning_system"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> str:
        """URL kết nối MySQL qua driver PyMySQL."""
        return (
            f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}"
        )


settings = Settings()
