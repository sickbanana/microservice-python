import pytest
from ..schemas.models import AddressDate


@pytest.mark.asyncio
async def test_create_address_api(get_client):
    response = await get_client.post("/api/tron", json={'address': 'TU3kjFuhtEo42tsCBtfYUAZxoqQ4yuSLQ5'})
    assert response.status_code == 200
    response = await get_client.get('/api/tron')
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert AddressDate.model_validate(body[0])
    assert body[0]['address'] == 'TU3kjFuhtEo42tsCBtfYUAZxoqQ4yuSLQ5'