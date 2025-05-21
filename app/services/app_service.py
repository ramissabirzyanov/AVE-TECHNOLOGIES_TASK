from typing import Optional

from redis.asyncio import Redis

from app.services.redis_service import RedisService
from app.api.schemas import DataSchema, AddressSchema


# Хотя в рамках этой задачи слой Service может выглядеть избыточным,
# он изолирует бизнес-логику и работу с Redis,
# не допуская прямого обращения к БД из вьюх.


class AppService:
    def __init__(self, redis: Redis):
        self.redis = RedisService(redis)

    async def write_data(self, data: DataSchema):
        await self.redis.write_data(data.phone, data.address)

    async def update_data_by_phone(self, phone: str, data: AddressSchema):
        if not await self.redis.is_key_exist(phone):
            raise KeyError(f"There is no such phone number: {phone}")
        await self.redis.write_data(phone, data.address)

    async def check_data_by_phone(self, phone: str) -> Optional[str]:
        data = await self.redis.check_data_by_phone(phone)
        return data

    async def is_phone_exist(self, phone: str) -> bool:
        return await self.redis.is_key_exist(key=phone)
