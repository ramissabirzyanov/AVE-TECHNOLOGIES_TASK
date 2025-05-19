from redis.asyncio import Redis

from app.api.schemas import Data
from app.core.settings import settings


class RedisService:
    def __init__(self):
        self.redis = Redis(
            host=settings.REDISHOST,
            port=settings.REDISPORT,
            db=settings.DB,
            decode_responses=settings.DECODE
        )
    
    async def write_data(self, data: Data):
        await self.redis.set(**data)

    async def check_data_by_phone(self, phone):
        address = await self.redis.get(phone)
        return address
