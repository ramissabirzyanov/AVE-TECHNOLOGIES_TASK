import pytest
import httpx

from app.main import app
from app.services.redis_service import redis


@pytest.fixture(autouse=True)
async def clear_redis():
    await redis.flushdb()

@pytest.fixture
async def async_client():

    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        yield client

