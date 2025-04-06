from tronpy import Tron
from tronpy.providers import HTTPProvider

from .schemas.models import Account
from .settings import API_KEY


provider = HTTPProvider(api_key=API_KEY)
client = Tron(provider=provider)


def get_tron_account_info(address: str) -> Account:
    account = client.get_account(address)
    return Account(
        balance_trx=account["balance"],
        bandwidth=account.get("net_usage", 0),
        energy=account.get("account_resource", {}).get("energy_usage", 0)
    )