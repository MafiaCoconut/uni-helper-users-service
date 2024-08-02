from abc import abstractmethod, ABC

from sqlalchemy.ext.asyncio import AsyncSession

from application.repositories.users_repository import UsersRepository
from domain.entities.user import User
from infrastructure.db.base import async_session_factory
from infrastructure.db.models.user_orm import UserOrm
from infrastructure.config.logs_config import log_decorator
from sqlalchemy import select, delete, update, asc


class UsersRepositoryImpl(UsersRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    @log_decorator
    async def save(self, user: User) -> None:
        async with self.session.begin():
            user_orm = UserOrm(
                user_id=user.user_id,
                username=user.username,
                name=user.name,
                mailing_time=user.mailing_time,
                locale=user.locale,
                canteen_id=user.canteen_id,
            )
            self.session.add(user_orm)
            await self.session.commit()

    @log_decorator
    async def save_many(self, users: list[User]) -> None:
        async with self.session.begin():
            for user in users:
                user_orm = UserOrm(
                    user_id=user.user_id,
                    username=user.username,
                    name=user.name,
                    mailing_time=user.mailing_time,
                    locale=user.locale,
                    canteen_id=user.canteen_id,
                )
                self.session.add(user_orm)
                await self.session.commit()

    @log_decorator
    async def get_users_all(self, ) -> list[User]:
        async with self.session.begin():
            query = await self.session.execute(select(UserOrm).order_by(asc(UserOrm.created_at)))
            res = query.scalars().all()
            return res

    @log_decorator
    async def get_user_by_user_id(self, user_id: int) -> User:
        async with self.session.begin():
            query = select(UserOrm).where(UserOrm.user_id == user_id)
            res = await self.session.execute(query)
            user = res.scalars().first()
            return user

    @log_decorator
    async def get_mailing_time_by_user_id(self, user_id: int) -> str:
        async with self.session.begin():
            query = select(UserOrm.mailing_time).where(UserOrm.user_id == user_id)
            result = await self.session.execute(query)
            return result.scalars().first()

    @log_decorator
    async def get_language_by_user_id(self, user_id: int) -> str:
        async with self.session.begin():
            query = select(UserOrm.locale).where(UserOrm.user_id == user_id)
            result = await self.session.execute(query)
            return result.scalars().first()

    @log_decorator
    async def get_canteen_id_by_user_id(self, user_id: int) -> int:
        async with self.session.begin():
            query = select(UserOrm.canteen_id).where(UserOrm.user_id == user_id)
            result = await self.session.execute(query)
            return result.scalars().first()

    @log_decorator
    async def get_status_by_user_id(self, user_id: int) -> str:
        async with self.session.begin():
            query = select(UserOrm.status).where(UserOrm.user_id == user_id)
            result = await self.session.execute(query)
            return result.scalars().first()

    @log_decorator
    async def check_existence(self, user_id: int) -> bool:
        async with self.session.begin():
            query = select(UserOrm.user_id).where(UserOrm.user_id == user_id)
            result = await self.session.execute(query)
            return result.scalars().first() is not None

    @log_decorator
    async def delete_user(self, user_id: int):
        async with self.session.begin():
            query = delete(UserOrm).where(UserOrm.user_id == user_id)
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def delete_all(self,):
        async with self.session.begin():
            query = delete(UserOrm)
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def update_mailing_time(self, user_id: int, mailing_time: str):
        async with self.session.begin():
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(mailing_time=mailing_time)
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def update_locale(self, user_id: int, locale: str):
        async with self.session.begin():
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(locale=locale)
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def update_canteen_id(self, user_id: int, canteen_id: int):
        async with self.session.begin():
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(canteen_id=canteen_id)
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def update_status(self, user_id: int, status: str):
        async with self.session.begin():
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(status=status)
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def deactivate_user(self, user_id: int):
        async with self.session.begin():
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(status='deactivated')
            await self.session.execute(query)
            await self.session.commit()

    @log_decorator
    async def reactivate_user(self, user_id: int):
        async with self.session.begin():
            query = update(UserOrm).where(UserOrm.user_id == user_id).values(status='active')
            await self.session.execute(query)
            await self.session.commit()

