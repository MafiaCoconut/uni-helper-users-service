from fastapi import Depends, APIRouter

from domain.entities.user import User
from infrastructure.config.services_config import users_service
router = APIRouter()


@router.post('/users/')
async def add_user(user: User):
    user = User(**user.model_dump())
    await users_service.save_user(user=user)
    return {"message": "User added successfully"}


@router.put('/users/{user_id}')
async def update_user(user_id: int, new_mailing_time: str = None, new_language: str = None, new_canteen_id: int = None):
    result = ""
    if new_mailing_time is not None:
        await users_service.update_mailing_time(user_id=user_id, mailing_time=new_mailing_time)
        result += "Mailing time updated successfully\n"

    if new_language is not None:
        await users_service.update_language(user_id=user_id, language=new_language)
        result += "Language updated successfully\n"

    if new_canteen_id is not None:
        await users_service.update_canteen_id(user_id=user_id, canteen_id=new_canteen_id)
        result += "Canteen_id updated successfully\n"

    return {"text": result}


@router.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    user = await users_service.get_user(user_id=user_id)
    return user



