from app.services.app_service import AppService


async def test_write_data(client):
    service = AppService()
    response = await client.post("/write_data", json={
        "phone": "89090000000",
        "address": "г. Москва, ул. Примерная, д. 1"
    })
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    value = await service.get("89090000000")
    assert value == "г. Москва, ул. Примерная, д. 1"


async def test_get_existing_data(client):
    service = AppService()
    await service.set("123", "г. Казань")
    response = await client.get("/check_data", params={"phone": "123"})
    assert response.status_code == 200
    assert response.json() == {"address": "г. Казань"}


async def test_get_non_existing_data(client):
    response = await client.get("/check_data", params={"phone": "000"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Phone not found"}
