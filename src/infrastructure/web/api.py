from fastapi import Depends, APIRouter

from domain.entities.user import User
from infrastructure.config.services_config import users_service
router = APIRouter()


@router.post('/users/')
def add_user(user: User):
    user = User(**user.model_dump())
    users_service.save_user(user=user)
    return {"message": "User added successfully"}


@router.put('/users/{user_id}')
def update_user(user: User):
    user = User(**user.model_dump())
    users_service.update_user(user=user)
    return {"message": "User updated successfully"}
