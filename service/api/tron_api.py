from fastapi import APIRouter, HTTPException, Depends, Body, Query
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..database.connection import get_session
from ..database.models import AddressRequest
from ..schemas.models import Address, AddressDate, Account
from ..tron import get_tron_account_info

tron = APIRouter()


@tron.post("", status_code=200)
async def address_info(address: Address, session: AsyncSession = Depends(get_session)):
    account = get_tron_account_info(address.address)
    async with session.begin():
        await session.execute(insert(AddressRequest).values(address=address.address))
    return account


@tron.get("", status_code=200)
async def get_requests_history(page: int = Query(1), per_page: int = Query(10, ge=1), session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(
            AddressRequest.address,
            AddressRequest.created_at
        )
        .offset((page - 1) * per_page)
        .limit(per_page)
    )
    result = [AddressDate(address=row.address, created_at=row.created_at) for row in result.mappings()]
    return result
