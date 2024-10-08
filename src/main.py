from fastapi import FastAPI

from infrastructure.config import logs_config
from infrastructure.db.base import Base, sync_engine
from infrastructure.web.api import router
from contextlib import asynccontextmanager
from infrastructure.db.models.user_orm import UserOrm
from infrastructure.config.services_config import get_scheduler_service


@asynccontextmanager
async def lifespan(app):
    logs_config.config()
    scheduler_service = get_scheduler_service()
    await scheduler_service.set_start_jobs()

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)


if __name__ == '__main__':
    Base.metadata.create_all(sync_engine)
