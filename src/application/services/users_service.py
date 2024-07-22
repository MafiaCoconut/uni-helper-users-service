from icecream import ic

from application.repositories.users_repository import UsersRepository
from application.validators.users_validator import UsersValidator
from domain.entities.user import User


class UsersService:
    def __init__(self,
                 users_repository: UsersRepository,
                 ):
        self.users_repository = users_repository

    async def save_user(self, user: User):
        await self.users_repository.save(user=user)

    async def get_user(self, user_id: int | str) -> User:
        return await self.users_repository.get_user_by_user_id(user_id=user_id)

    async def get_all_users(self) -> list[User]:
        return await self.users_repository.get_users_all()

    async def get_mailing_time(self, user_id: int | str):
        res = await self.users_repository.get_mailing_time_by_user_id(user_id=user_id)
        return res

    async def get_language(self, user_id: int | str):
        return await self.users_repository.get_language_by_user_id(user_id=user_id)

    async def get_canteen_id(self, user_id: int | str):
        return await self.users_repository.get_canteen_id_by_user_id(user_id=user_id)

    async def save_many_users(self, users: list[User]):
        # self.users_validator.validate_users(users)
        await self.users_repository.save_many(users=users)

    async def delete_user(self, user_id: int | str):
        await self.users_repository.delete_user(user_id=user_id)

    async def delete_all_users(self):
        await self.users_repository.delete_all()

    async def update_mailing_time(self, user_id: int | str, mailing_time: str):
        await self.users_repository.update_mailing_time(user_id=user_id, mailing_time=mailing_time)

    async def update_language(self, user_id: int | str, language: str):
        await self.users_repository.update_language(user_id=user_id, language=language)

    async def update_canteen_id(self, user_id: int | str, canteen_id: int):
        await self.users_repository.update_canteen_id(user_id=user_id, canteen_id=canteen_id)


