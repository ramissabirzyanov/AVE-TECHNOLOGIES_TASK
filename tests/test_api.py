import pytest


@pytest.mark.asyncio
async def test_check_data_returns_404(async_client):
    response = await async_client.get("/check_data?phone=000")
    assert response.status_code == 404
    assert response.json() == {'detail': 'No data for 000'}


@pytest.mark.asyncio
async def test_write_data(async_client):
    response = await async_client.post(url="/write_data", json={"phone": "333", "address": "г. Казань"})
    assert response.status_code == 200
    assert response.json() ==  {"status": "Data was written."}
    address = await async_client.get("/check_data?phone=333")
    assert address.json() == {"address": "г. Казань"}
