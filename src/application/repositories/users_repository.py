from abc import abstractmethod, ABC

from src.domain.entities.user import User


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

