from abc import abstractmethod, ABC

from domain.entities.user import User


class UsersRepository(ABC):

    @staticmethod
    @abstractmethod
    def save(user: User) -> None:
        pass

    @staticmethod
    @abstractmethod
    def save_many(users: list[User]) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_users_all() -> list[User]:
        pass

    @staticmethod
    @abstractmethod
    def get_mailing_time_by_user_id(user_id: int) -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_user_by_user_id(user_id: int) -> User:
        pass

    @staticmethod
    @abstractmethod
    def get_language_by_user_id(user_id: int) -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_canteen_id_by_user_id(user_id: int) -> User:
        pass

    @staticmethod
    @abstractmethod
    def delete_user(user_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_all():
        pass

    @staticmethod
    @abstractmethod
    def update_mailing_time(user_id: int | str, mailing_time: str):
        pass

    @staticmethod
    @abstractmethod
    def update_language(user_id: int | str, language: str):
        pass

    @staticmethod
    @abstractmethod
    def update_canteen_id(user_id: int | str, canteen_id: int):
        pass
