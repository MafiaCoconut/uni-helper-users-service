import time
from contextlib import asynccontextmanager
import shutil

from infrastructure.config.logs_config import log_decorator


class S3UseCase:
    def __init__(self, s3_client):
        self.s3_client = s3_client

    @log_decorator
    async def upload_file(self, file_path: str, file_name: str):
        await self.s3_client.upload_file(file_path=file_path, file_name=file_name)

    @log_decorator
    async def upload_logs(self):
        logs_files = {
            "users_system_logs.txt": "logs/system_data.log",
            "users_error_logs.txt": "logs/error_data.log",
        }
        for file_name, file_path in logs_files.items():
            await self.s3_client.upload_file(file_path=file_path, file_name=file_name)

