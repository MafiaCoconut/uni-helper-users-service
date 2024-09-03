from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.users_repository import UsersRepository
from infrastructure.config.repositories_config import get_users_repository


class RepositoriesProviderImpl(RepositoriesProvider):
    def get_users_repository(self) -> UsersRepository:
        return get_users_repository()