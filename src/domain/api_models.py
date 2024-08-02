from pydantic import BaseModel


class UpdateUserData(BaseModel):
    new_mailing_time: str | None = None
    new_locale: str | None = None
    new_canteen_id: int | None = None
