from pydantic import BaseModel, Field


class Address(BaseModel):
    address: str


class Account(BaseModel):
    balance_trx: int
    bandwidth: int
    energy: int