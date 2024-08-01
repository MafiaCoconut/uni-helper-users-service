from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.base import async_engine
from infrastructure.repositories_impl.users_repository_impl import UsersRepositoryImpl


def get_users_repository() -> UsersRepositoryImpl:
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return UsersRepositoryImpl(session=session)
# users_repository = UsersRepositoryImpl()

