from abc import abstractmethod, ABC

from application.repositories.users_repository import UsersRepository
from domain.entities.user import User
from infrastructure.db.base import async_session_factory
from infrastructure.db.models.user_orm import UserOrm
from infrastructure.config.logs_config import log_decorator
from sqlalchemy import select, delete, update, asc


class UsersRepositoryImpl(UsersRepository):
    @staticmethod
    @log_decorator
    async def save(user: User) -> None:
        async with async_session_factory() as session:
            user_orm = UserOrm(
                user_id=user.user_id,
                username=user.username,
                mailing_time=user.mailing_time,
                language=user.language,
                canteen_id=user.canteen_id,
            )
            session.add(user_orm)
            await session.commit()

    @staticmethod
    @log_decorator
    async def save_many(users: list[User]) -> None:
        async with async_session_factory() as session:
            for user in users:
                user_orm = UserOrm(
                    user_id=user.user_id,
                    username=user.username,
                    mailing_time=user.mailing_time,
                    language=user.language,
                    canteen_id=user.canteen_id,
                )
                session.add(user_orm)
                await session.commit()

    @staticmethod
    @log_decorator
    async def get_users_all() -> list[User]:
        async with async_session_factory() as session:
            query = await session.execute(select(UserOrm).order_by(asc(UserOrm.created_at)))
            res = query.scalars().all()
            return res
            # return [User(
            #     user_id=user.user_id,
            #     username=user.username,
            #     mailing_time=user.mailing_time,
            #     language=user.language,
            #     canteen_id=user.canteen_id,
            #     created_at=user.created_at,
            #     updated_at=user.updated_at,
            #     status=user.status,
            # ) for user in res]

    @staticmethod
    @log_decorator
    async def get_user_by_user_id(user_id: int) -> User:
        async with async_session_factory() as session:
            query = select(UserOrm).where(UserOrm.user_id == user_id)
            res = await session.execute(query)
            user = res.scalars().first()
            return (user)
            # return User(
            #     user_id=user.user_id,
            #     username=user.username,
            #     mailing_time=user.mailing_time,
            #     language=user.language,
            #     canteen_id=user.canteen_id,
            #     created_at=user.created_at,
            #     updated_at=user.updated_at,
            #     status=user.status,
            # )

    @staticmethod
    @log_decorator
    async def get_mailing_time_by_user_id(user_id: int) -> str:
        async with async_session_factory() as session:
            query = select(UserOrm.mailing_time).where(UserOrm.user_id == user_id)
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    @log_decorator
    async def get_language_by_user_id(user_id: int) -> str:
        async with async_session_factory() as session:
            query = select(UserOrm.language).where(UserOrm.user_id == user_id)
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    @log_decorator
    async def get_canteen_id_by_user_id(user_id: int) -> int:
        async with async_session_factory() as session:
            query = select(UserOrm.canteen_id).where(UserOrm.user_id == user_id)
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    @log_decorator
    async def get_status_by_user_id(user_id: int) -> str:
        async with async_session_factory() as session:
            query = select(UserOrm.status).where(UserOrm.user_id == user_id)
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    @log_decorator
    async def delete_user(user_id: int):
        async with async_session_factory() as session:
            query = delete(UserOrm).where(UserOrm.user_id == user_id)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def delete_all():
        async with async_session_factory() as session:
            query = delete(UserOrm)
            await session.execute(query)
            await session.commit()


    @staticmethod
    @log_decorator
    async def update_mailing_time(user_id: int, mailing_time: str):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(mailing_time=mailing_time)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def update_language(user_id: int, language: str):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(language=language)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def update_canteen_id(user_id: int, canteen_id: int):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(canteen_id=canteen_id)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def update_status(user_id: int, status: str):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(status=status)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def deactivate_user(user_id: int):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(status='deactivated')
            await session.execute(query)
            await session.commit()
