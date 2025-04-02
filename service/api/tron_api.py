from typing import Dict
from tronpy import Tron
from tronpy.keys import PrivateKey
from fastapi import APIRouter, HTTPException
from tronpy.providers import HTTPProvider

tron = APIRouter()


def get_tron_account_info(address: str):
    provider = HTTPProvider(api_key=bytes.fromhex("8888888888888888888888888888888888888888888888888888888888888888"))
    client = Tron(provider=provider)

    try:
        account = client.get_account(address)
        balance_trx = account["balance"]
        bandwidth = account.get("net_usage", 0)
        energy = account.get("account_resource", {}).get("energy_usage", 0)
        response = account
        return response

    except Exception as e:
        print(f"Ошибка: {e}")


@tron.post("/", response_model=Dict, status_code=200)
async def address_info(address: str):
    print(address)
    return get_tron_account_info(address)