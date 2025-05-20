from typing import Optional

from redis.asyncio import Redis


class RedisService:
    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def is_key_exist(self, key: str) -> bool:
        exists = await self.redis_client.exists(key)
        return bool(exists)

    async def write_data(self, phone: str, address: str):
        await self.redis_client.set(phone, address)

    async def check_data_by_phone(self, phone: str) -> Optional[str]:
        data = await self.redis_client.get(phone)
        return data
