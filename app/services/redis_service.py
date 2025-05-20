from redis.asyncio import Redis

from app.api.schemas import DataSchema


class RedisService:
    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def write_data(self, data: DataSchema):
        await self.redis_client.set(data.phone, data.address)

    async def check_data_by_phone(self, phone):
        data = await self.redis_client.get(phone)
        return data
