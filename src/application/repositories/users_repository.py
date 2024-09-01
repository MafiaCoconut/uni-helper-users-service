from abc import abstractmethod, ABC

from domain.entities.user import User


class UsersRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def save_many(self, users: list[User]) -> None:
        pass

    @abstractmethod
    async def get_users_all(self, ) -> list[User]:
        pass

    @abstractmethod
    async def get_mailing_time_by_user_id(self, user_id: int) -> str:
        pass

    @abstractmethod
    async def get_user_by_user_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def get_language_by_user_id(self, user_id: int) -> str:
        pass

    @abstractmethod
    async def get_canteen_id_by_user_id(self, user_id: int) -> int:
        pass

    @abstractmethod
    async def get_status_by_user_id(self, user_id: int) -> str:
        pass

    @abstractmethod
    async def check_existence(self, user_id: int) -> bool:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int):
        pass

    @abstractmethod
    async def delete_all(self, ):
        pass

    @abstractmethod
    async def update_mailing_time(self, user_id: int, mailing_time: str):
        pass

    @abstractmethod
    async def update_locale(self, user_id: int, locale: str):
        pass

    @abstractmethod
    async def update_canteen_id(self, user_id: int, canteen_id: int):
        pass

    @abstractmethod
    async def update_status(self, user_id: int, status: str):
        pass

    @abstractmethod
    async def deactivate_user(self, user_id: int):
        pass

    @abstractmethod
    async def reactivate_user(self, user_id: int):
        pass




