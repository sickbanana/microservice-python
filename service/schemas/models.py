from datetime import datetime
from pydantic import BaseModel, Field


class Address(BaseModel):
    address: str


class AddressDate(Address):
    created_at: datetime


class Account(BaseModel):
    balance_trx: int
    bandwidth: int
    energy: int