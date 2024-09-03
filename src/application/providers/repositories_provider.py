from abc import ABC, abstractmethod

from application.repositories.users_repository import UsersRepository


class RepositoriesProvider(ABC):
    @abstractmethod
    def get_users_repository(self) -> UsersRepository:
        pass