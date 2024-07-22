from icecream import ic

from application.repositories.users_repository import UsersRepository
from application.validators.users_validator import UsersValidator
from domain.entities.user import User


class UsersService:
    def __init__(self,
                 users_repository: UsersRepository,
                 ):
        self.users_repository = users_repository

    def save_user(self, user: User):
        self.users_repository.save(user=user)

    def get_user(self, user_id: int | str) -> User:
        return self.users_repository.get_user_by_user_id(user_id=user_id)

    def get_all_users(self) -> list[User]:
        return self.users_repository.get_users_all()

    def get_mailing_time(self, user_id: int | str):
        res = self.users_repository.get_mailing_time_by_user_id(user_id=user_id)
        return res

    def get_language(self, user_id: int | str):
        return self.users_repository.get_language_by_user_id(user_id=user_id)

    def get_canteen_id(self, user_id: int | str):
        return self.users_repository.get_canteen_id_by_user_id(user_id=user_id)

    def save_many_users(self, users: list[User]):
        # self.users_validator.validate_users(users)
        self.users_repository.save_many(users=users)

    def delete_user(self, user_id: int | str):
        self.users_repository.delete_user(user_id=user_id)

    def delete_all_users(self):
        self.users_repository.delete_all()

    def update_mailing_time(self, user_id: int | str, mailing_time: str):
        self.users_repository.update_mailing_time(user_id=user_id, mailing_time=mailing_time)

    def update_language(self, user_id: int | str, language: str):
        self.users_repository.update_language(user_id=user_id, language=language)

    def update_canteen_id(self, user_id: int | str, canteen_id: int):
        self.users_repository.update_canteen_id(user_id=user_id, canteen_id=canteen_id)


