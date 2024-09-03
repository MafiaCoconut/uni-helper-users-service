from icecream import ic

from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.users_repository import UsersRepository
from application.validators.users_validator import UsersValidator
from domain.entities.user import User


class UsersService:
    def __init__(self,
                 repositories_provider: RepositoriesProvider,
                 ):
        self.repositories_provider = repositories_provider

    async def save_user(self, user: User):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.save(user=user)

    async def get_user(self, user_id: int) -> User:
        users_repository = self.repositories_provider.get_users_repository()
        return await users_repository.get_user_by_user_id(user_id=user_id)

    async def get_all_users(self) -> list[User]:
        users_repository = self.repositories_provider.get_users_repository()
        return await users_repository.get_users_all()

    async def get_mailing_time(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        res = await users_repository.get_mailing_time_by_user_id(user_id=user_id)
        return res

    async def get_language(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        return await users_repository.get_language_by_user_id(user_id=user_id)

    async def get_canteen_id(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        return await users_repository.get_canteen_id_by_user_id(user_id=user_id)

    async def check_existence(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        return await users_repository.check_existence(user_id=user_id)

    async def save_many_users(self, users: list[User]):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.save_many(users=users)

    async def delete_user(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.delete_user(user_id=user_id)

    async def delete_all_users(self):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.delete_all()

    async def update_mailing_time(self, user_id: int, mailing_time: str):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.update_mailing_time(user_id=user_id, mailing_time=mailing_time)

    async def update_language(self, user_id: int, locale: str):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.update_locale(user_id=user_id, locale=locale)

    async def update_canteen_id(self, user_id: int, canteen_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.update_canteen_id(user_id=user_id, canteen_id=canteen_id)

    async def update_status(self, user_id: int, status: str):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.update_status(user_id=user_id, status=status)
        
    async def deactivate_user(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.deactivate_user(user_id=user_id)

    async def reactivate_user(self, user_id: int):
        users_repository = self.repositories_provider.get_users_repository()
        await users_repository.reactivate_user(user_id=user_id)





