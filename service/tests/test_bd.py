import pytest
from sqlalchemy import insert, select

from ..database.models import AddressRequest


@pytest.mark.asyncio
async def test_create_address(get_test_session):
    async with get_test_session.begin():
        await get_test_session.execute(insert(AddressRequest).values(address='TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK'))

    result = await get_test_session.execute(select(AddressRequest.address))
    addresses = result.all()
    assert len(addresses) == 1
    assert addresses[0].address == 'TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK'