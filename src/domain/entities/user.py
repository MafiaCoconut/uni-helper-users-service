from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    user_id: int = field(default=None)
    username: str = field(default=None)
    mailing_time: str = field(default=None)
    language: str = field(default=None)
    canteen_id: int = field(default=None)
    updated_at: datetime = field(default=None)
    created_at: datetime = field(default=None)
