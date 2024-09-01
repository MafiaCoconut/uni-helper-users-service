from application.services.users_service import UsersService
from infrastructure.config.repositories_config import get_users_repository
from infrastructure.config.validators_config import users_validator
from application.services.s3_service import S3Service
from application.services.scheduler_service import SchedulerService
from infrastructure.config.s3_config import s3client
from infrastructure.config.scheduler_interfaces_config import get_scheduler_interface


s3_service = S3Service(
    s3client=s3client
)


def get_scheduler_service() -> SchedulerService:
    return SchedulerService(
        scheduler_interface=get_scheduler_interface(),
        s3_service=s3_service
    )


def get_users_service() -> UsersService:
    return UsersService(
        users_repository=get_users_repository(),
    )
