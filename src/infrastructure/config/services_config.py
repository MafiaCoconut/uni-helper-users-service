from application.services.users_service import UsersService
from infrastructure.config.repositories_config import users_repository
from infrastructure.config.validators_config import users_validator

users_service = UsersService(
    users_repository=users_repository,
)
