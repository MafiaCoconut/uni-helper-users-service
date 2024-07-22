from fastapi import FastAPI

from infrastructure.config import logs_config
from infrastructure.db.base import Base, sync_engine
from infrastructure.web.api import router
from contextlib import asynccontextmanager
from infrastructure.db.models.user_orm import UserOrm
app = FastAPI()

app.include_router(router)


@asynccontextmanager
async def lifespan(app):
    logs_config.config()


if __name__ == '__main__':
    pass
    # Base.metadata.create_all(sync_engine)
