import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AddressRequest(Base):
    __tablename__ = 'address_request'

    id = sa.Column(sa.types.Integer, primary_key=True, unique=True, autoincrement=True)
    address = sa.Column(sa.types.String, nullable=False)
    created_at = sa.Column(sa.types.DateTime, server_default=sa.func.now())
