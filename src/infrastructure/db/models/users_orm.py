from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, ForeignKey

from datetime import datetime
from src.infrastructure.db.base import Base
from src.infrastructure.db.models.orm_template_columns import intpk, created_at, updated_at


class UsersOrm(Base):
    __tablename__ = 'users'

    user_id: Mapped[intpk]
    username: Mapped[str]
    mailing_time: Mapped[datetime]
    language: Mapped[str]
    canteen_id: Mapped[int] == mapped_column(ForeignKey("canteens.canteen_id"))
    updated_at: Mapped[updated_at]
    created_at: Mapped[created_at]
