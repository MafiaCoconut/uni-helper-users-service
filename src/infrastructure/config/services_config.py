from src.application.services.users_service import UsersService
from src.infrastructure.config.repositories_config import users_repository
from src.infrastructure.config.validators_config import users_validator

users_service = UsersService(
    users_repository=users_repository,
    users_validator=users_validator,
)
