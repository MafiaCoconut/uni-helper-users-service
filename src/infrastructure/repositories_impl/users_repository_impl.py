from abc import abstractmethod, ABC

from application.repositories.users_repository import UsersRepository
from domain.entities.user import User
from infrastructure.db.base import async_session_factory
from infrastructure.db.models.user_orm import UserOrm
from infrastructure.config.logs_config import log_decorator
from sqlalchemy import select, delete, update


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
            query = await session.execute(select(UserOrm))
            res = query.scalars().all()

            return [User(
                user_id=user.user_id,
                username=user.username,
                mailing_time=user.mailing_time,
                language=user.language,
                canteen_id=user.canteen_id,
            ) for user in res]

    @staticmethod
    @log_decorator
    async def get_user_by_user_id(user_id: int) -> User:
        async with async_session_factory() as session:
            query = select(UserOrm).filter(UserOrm.user_id == user_id)
            await session.execute(query)
            user = session.scalars().all()
            return User(
                user_id=user.user_id,
                username=user.username,
                mailing_time=user.mailing_time,
                language=user.language,
                canteen_id=user.canteen_id,
            )

    @staticmethod
    @log_decorator
    async def get_mailing_time_by_user_id(user_id: int | str) -> str:
        async with async_session_factory() as session:
            query = select(UserOrm.mailing_time).where(UserOrm.user_id == user_id)
            await session.execute(query)
            return session.scalars().all()

    @staticmethod
    @log_decorator
    async def get_language_by_user_id(user_id: int | str) -> str:
        async with async_session_factory() as session:
            query = select(UserOrm.language).where(UserOrm.user_id == user_id)
            await session.execute(query)
            return session.scalars().all()

    @staticmethod
    @log_decorator
    async def get_canteen_id_by_user_id(user_id: int | str) -> User:
        async with async_session_factory() as session:
            query = select(UserOrm.canteen_id).where(UserOrm.user_id == user_id)
            await session.execute(query)
            return session.scalars().all()

    @staticmethod
    @log_decorator
    async def delete_user(user_id: int | str):
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
    async def update_mailing_time(user_id: int | str, mailing_time: str):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(mailing_time=mailing_time)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def update_language(user_id: int | str, language: str):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(language=language)
            await session.execute(query)
            await session.commit()

    @staticmethod
    @log_decorator
    async def update_canteen_id(user_id: int | str, canteen_id: int):
        async with async_session_factory() as session:
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(canteen_id=canteen_id)
            await session.execute(query)
            await session.commit()
