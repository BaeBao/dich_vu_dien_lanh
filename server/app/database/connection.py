"""Thiết lập SQLAlchemy engine và session cho MySQL."""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    """Base class cho các model SQLAlchemy."""


# Engine chỉ kết nối khi ứng dụng thực sự truy vấn Database.
engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator[Session, None, None]:
    """Cung cấp một Database session cho mỗi request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
