from abc import abstractmethod, ABC

from src.domain.entities.user import User
from src.infrastructure.db.base import async_session_factory
from src.infrastructure.db.models.user_orm import UserOrm

from sqlalchemy import select, delete


class UsersRepository(ABC):
    @staticmethod
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
    def get_user_by_user_id(user_id: int) -> User:
        with async_session_factory() as session:
            query = select(UserOrm).filter(UserOrm.user_id == int(user_id))
            session.execute(query)
            return session.scalars().all()

    @staticmethod
    def get_mailing_time_by_user_id(user_id: int) -> str:
        with async_session_factory() as session:
            query = select(UserOrm.mailing_time).filter(UserOrm.user_id == int(user_id))
            session.execute(query)
            return session.scalars().all()

    @staticmethod
    def get_language_by_user_id(user_id: int) -> str:
        with async_session_factory() as session:
            query = select(UserOrm.language).filter(UserOrm.user_id == int(user_id))
            session.execute(query)
            return session.scalars().all()

    @staticmethod
    def get_canteen_id_by_user_id(user_id: int) -> User:
        with async_session_factory() as session:
            query = select(UserOrm.canteen_id).filter(UserOrm.user_id == int(user_id))
            session.execute(query)
            return session.scalars().all()

