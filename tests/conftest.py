import pytest_asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from redis.asyncio import Redis

from app.api.dependencies import get_service
from app.main import app
from app.services.app_service import AppService



@pytest_asyncio.fixture
async def redis_client():
    redis = Redis(
        host="localhost",
        port=6379,
        db=10,  # тестовая бд
        decode_responses=True,
    )
    await redis.flushdb()
    yield redis
    await redis.aclose()


@pytest_asyncio.fixture
async def async_client(redis_client):
    async def override_get_service():
        return AppService(redis_client)

    app.dependency_overrides[get_service] = override_get_service

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()

