from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    user_id: int
    username: str
    mailing_time: datetime
    language: str
    canteen_id: int
    updated_at: datetime
    created_at: datetime
