# from dataclasses import dataclass, field
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str = '-'
    mailing_time: str = '-'
    language: str = '-'
    canteen_id: int = 0
    created_at: datetime
    updated_at: datetime
