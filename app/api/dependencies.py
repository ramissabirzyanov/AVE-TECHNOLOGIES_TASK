from redis.asyncio import Redis

from app.core.settings import settings
from app.services.app_service import AppService



async def get_service() -> AppService:
    redis = Redis(
        host=settings.REDISHOST,
        port=settings.REDISPORT,
        db=settings.DB,
        decode_responses=settings.DECODE
    )
    return AppService(redis)