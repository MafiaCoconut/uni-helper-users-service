from abc import abstractmethod, ABC

from domain.entities.user import User


class UsersRepository(ABC):

    @staticmethod
    @abstractmethod
    async def save(user: User) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def save_many(users: list[User]) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def get_users_all() -> list[User]:
        pass

    @staticmethod
    @abstractmethod
    async def get_mailing_time_by_user_id(user_id: int) -> str:
        pass

    @staticmethod
    @abstractmethod
    async def get_user_by_user_id(user_id: int) -> User:
        pass

    @staticmethod
    @abstractmethod
    async def get_language_by_user_id(user_id: int) -> str:
        pass

    @staticmethod
    @abstractmethod
    async def get_canteen_id_by_user_id(user_id: int) -> int:
        pass

    @staticmethod
    @abstractmethod
    async def get_status_by_user_id(user_id: int) -> str:
        pass


    @staticmethod
    @abstractmethod
    async def delete_user(user_id: int):
        pass

    @staticmethod
    @abstractmethod
    async def delete_all():
        pass

    @staticmethod
    @abstractmethod
    async def update_mailing_time(user_id: int, mailing_time: str):
        pass

    @staticmethod
    @abstractmethod
    async def update_language(user_id: int, language: str):
        pass

    @staticmethod
    @abstractmethod
    async def update_canteen_id(user_id: int, canteen_id: int):
        pass

    @staticmethod
    @abstractmethod
    async def update_status(user_id: int, status: str):
        pass

    @staticmethod
    @abstractmethod
    async def deactivate_user(user_id: int):
        pass




