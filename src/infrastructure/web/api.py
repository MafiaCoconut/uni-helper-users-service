from fastapi import Depends, APIRouter, Response, status
from icecream import ic

from domain.api_models import UpdateUserData
from domain.entities.user import User
from infrastructure.config.logs_config import log_api_decorator
from infrastructure.config.services_config import get_users_service

router = APIRouter()


@router.put('/user{user_id}/updateData')
@log_api_decorator
async def update_user(
        user_id: int, data: UpdateUserData,
        response: Response, users_service=Depends(get_users_service)
):
    result = ""
    error = ""
    ic(data.new_locale, data.new_canteen_id, data.new_mailing_time)
    if await users_service.check_existence(user_id=user_id):
        if data.new_mailing_time is not None:
            await users_service.update_mailing_time(user_id=user_id, mailing_time=data.new_mailing_time)
            result += "Mailing time updated successfully\n"

        if data.new_locale is not None:
            await users_service.update_language(user_id=user_id, locale=data.new_locale)
            result += "Locale updated successfully\n"

        if data.new_canteen_id is not None:
            await users_service.update_canteen_id(user_id=user_id, canteen_id=data.new_canteen_id)
            result += "Canteen_id updated successfully\n"

        # if data.status is not None:
        #     await users_service.update_status(user_id=user_id, status=data.status)
        #     result += "Status updated successfully\n"
    else:
        error = "UserNotExist"
        result = "The user does not exist"

    return {"text": result, "error": error}


@router.get('/user{user_id}/getData')
@log_api_decorator
async def get_user_by_id(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    user = await users_service.get_user(user_id=user_id)
    return user


@router.get('/user{user_id}/getMailingTime')
@log_api_decorator
async def get_mailing_time(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    return await users_service.get_mailing_time(user_id=user_id)


@router.get('/user{user_id}/getLanguage')
@log_api_decorator
async def get_language(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    return await users_service.get_language(user_id=user_id)


@router.get('/user{user_id}/getCanteenId')
@log_api_decorator
async def get_canteen_id(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    return await users_service.get_canteen_id(user_id=user_id)


@router.put('/user{user_id}/deactivate')
@log_api_decorator
async def deactivate_user(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    await users_service.deactivate_user(user_id=user_id)
    return {"text": "User deactivated successfully"}


@router.put('/user{user_id}/reactivate')
@log_api_decorator
async def reactivate_user(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    await users_service.update_status(user_id=user_id, status='active')
    return {"text": "User reactivated successfully"}


@router.post('/users/createUser')
@log_api_decorator
async def add_user(
        user: dict,
        response: Response, users_service=Depends(get_users_service)
):
    user = User.model_validate((user['user']))
    await users_service.save_user(user=user)
    return {"text": "User added successfully"}


@router.get('/users/getAll')
@log_api_decorator
async def get_all_users(
        response: Response, users_service=Depends(get_users_service)
):
    users = await users_service.get_all_users()
    return users


@router.get('/user{user_id}/checkExistence')
@log_api_decorator
async def check_existence(
        user_id: int,
        response: Response, users_service=Depends(get_users_service)
):
    return await users_service.check_existence(user_id=user_id)
