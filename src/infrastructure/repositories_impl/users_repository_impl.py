from abc import abstractmethod, ABC

from application.repositories.users_repository import UsersRepository
from domain.entities.user import User
from infrastructure.db.base import async_session_factory
from infrastructure.db.models.user_orm import UserOrm
from infrastructure.config.logs_config import log_decorator
from sqlalchemy import select, delete


class UsersRepositoryImpl(UsersRepository):
    @staticmethod
    @log_decorator
    def save(user: User) -> None:
        with async_session_factory() as session:
            user_orm = UserOrm(
                user_id=user.user_id,
                username=user.username,
                mailing_time=user.mailing_time,
                language=user.language,
                canteen_id=user.canteen_id,
            )
            session.add(user_orm)
            session.commit()

    @staticmethod
    @log_decorator
    def save_many(users: list[User]) -> None:
        with async_session_factory() as session:
            for user in users:
                user_orm = UserOrm(
                    user_id=user.user_id,
                    username=user.username,
                    mailing_time=user.mailing_time,
                    language=user.language,
                    canteen_id=user.canteen_id,
                )
                session.add(user_orm)
                session.commit()

    @staticmethod
    @log_decorator
    def get_users_all() -> list[User]:
        with async_session_factory() as session:
            query = session.execute(select(UserOrm))
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
    def get_user_by_user_id(user_id: int) -> User:
        with async_session_factory() as session:
            query = select(UserOrm).filter(UserOrm.user_id == int(user_id))
            session.execute(query)
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
    def get_mailing_time_by_user_id(user_id: int | str) -> str:
        with async_session_factory() as session:
            query = select(UserOrm.mailing_time).where(UserOrm.user_id == str(user_id))
            session.execute(query)
            return session.scalars().all()

    @staticmethod
    @log_decorator
    def get_language_by_user_id(user_id: int | str) -> str:
        with async_session_factory() as session:
            query = select(UserOrm.language).where(UserOrm.user_id == str(user_id))
            session.execute(query)
            return session.scalars().all()

    @staticmethod
    @log_decorator
    def get_canteen_id_by_user_id(user_id: int | str) -> User:
        with async_session_factory() as session:
            query = select(UserOrm.canteen_id).where(UserOrm.user_id == str(user_id))
            session.execute(query)
            return session.scalars().all()

    @staticmethod
    @log_decorator
    def delete_user(user_id: int | str):
        with async_session_factory() as session:
            query = delete(UserOrm).where(UserOrm.user_id == user_id)
            session.execute(query)
            session.commit()

    @staticmethod
    @log_decorator
    def delete_all():
        with async_session_factory() as session:
            query = delete(UserOrm)
            session.execute(query)
            session.commit()
