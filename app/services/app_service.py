from redis.asyncio import Redis

from app.services.redis_service import RedisService


# Хотя в рамках этой задачи слой Service может выглядеть избыточным,
# он изолирует бизнес-логику и работу с Redis,
# не допуская прямого обращения к БД из вьюх.


class AppService:
    def __init__(self, redis: Redis):
        self.redis = RedisService(redis)

    async def write_data(self, data):
        await self.redis.write_data(data)

    async def check_data_by_phone(self, phone):
        data = await self.redis.check_data_by_phone(phone)
        return data
