from httpx import AsyncClient


async def test_get_data_returns_404(async_client: AsyncClient):
    phone = "000"
    response = await async_client.get(f"/data/{phone}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"No data for {phone}"}


async def test_post_data(async_client: AsyncClient):
    response = await async_client.post(
        url="/data",
        json={"phone": "333", "address": "г. Казань"}
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Data was written."}


async def test_get_data(async_client):
    await async_client.post(
        url="/data",
        json={"phone": "123", "address": "г. Тестбург"}
    )
    response = await async_client.get("/data/123")
    assert response.status_code == 200
    assert response.json() == {"address": "г. Тестбург"}


async def test_update_data(async_client):
    await async_client.post(
        url="/data",
        json={"phone": "123", "address": "г. Тестбург"}
    )
    response = await async_client.put(
        url="/data/123",
        json={"address": "г. Тестград"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Data was rewritten."}
