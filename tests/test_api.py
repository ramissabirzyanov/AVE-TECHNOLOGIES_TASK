async def test_check_data_returns_404(async_client):
    response = await async_client.get("/check_data?phone=000")
    assert response.status_code == 404
    assert response.json() == {'detail': 'No data for 000'}


async def test_write_data(async_client):
    response = await async_client.post(
        url="/write_data",
        json={"phone": "333", "address": "г. Казань"}
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "Data was written."}


async def test_check_data(async_client):
    await async_client.post(
        url="/write_data",
        json={"phone": "123", "address": "г. Тестбург"}
    )
    response = await async_client.get("/check_data?phone=123")
    assert response.status_code == 200
    assert response.json() == {"address": "г. Тестбург"}


async def test_rewrite_data(async_client):
    await async_client.post(
        url="/write_data",
        json={"phone": "123", "address": "г. Тестбург"}
    )
    response = await async_client.post(
        url="/write_data",
        json={"phone": "123", "address": "г. Тестград"}
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "Data was rewritten."}
