from fastapi import Depends, APIRouter

from domain.entities.user import User
from infrastructure.config.services_config import users_service
router = APIRouter()


@router.put('/user{user_id}/updateData')
async def update_user(user_id: int, new_mailing_time: str = None,
                      new_locale: str = None, new_canteen_id: int = None,
                      status: str = None):
    result = ""
    if new_mailing_time is not None:
        await users_service.update_mailing_time(user_id=user_id, mailing_time=new_mailing_time)
        result += "Mailing time updated successfully\n"

    if new_locale is not None:
        await users_service.update_language(user_id=user_id, locale=new_locale)
        result += "Locale updated successfully\n"

    if new_canteen_id is not None:
        await users_service.update_canteen_id(user_id=user_id, canteen_id=new_canteen_id)
        result += "Canteen_id updated successfully\n"

    if status is not None:
        await users_service.update_status(user_id=user_id, status=status)
        result += "Status updated successfully\n"

    return {"text": result}


@router.get('/user{user_id}/getData')
async def get_user_by_id(user_id: int):
    user = await users_service.get_user(user_id=user_id)
    return user


@router.get('/user{user_id}/getMailingTime')
async def get_mailing_time(user_id: int):
    return await users_service.get_mailing_time(user_id=user_id)


@router.get('/user{user_id}/getLanguage')
async def get_language(user_id: int):
    return await users_service.get_language(user_id=user_id)


@router.get('/user{user_id}/getCanteenId')
async def get_canteen_id(user_id: int):
    return await users_service.get_canteen_id(user_id=user_id)


@router.put('/user{user_id}/deactivate')
async def deactivate_user(user_id: int):
    await users_service.deactivate_user(user_id=user_id)
    return {"text": "User deactivated successfully"}


@router.put('/user{user_id}/reactivate')
async def reactivate_user(user_id: int):
    await users_service.update_status(user_id=user_id, status='active')
    return {"text": "User reactivated successfully"}


@router.post('/users/createUser')
async def add_user(user: User):
    user = User(**user.model_dump())
    await users_service.save_user(user=user)
    return {"text": "User added successfully"}


@router.get('/users/getAll')
async def get_all_users():
    users = await users_service.get_all_users()
    return users



