from icecream import ic

from src.application.repositories.users_repository import UsersRepository
from src.application.validators.users_validator import UsersValidator
from src.domain.entities.user import User


class UsersService:
    def __init__(self,
                 users_repository: UsersRepository,
                 users_validator: UsersValidator,
                 ):
        self.users_repository = users_repository
        self.users_validator = users_validator

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

