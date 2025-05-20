from fastapi import Depends

from app.services.redis_service import RedisService
from app.services.app_service import AppService


async def get_redis_service() -> RedisService:
    return RedisService()


async def get_service(redis_service: RedisService = Depends(get_redis_service)) -> AppService:
    return AppService(redis_service)
