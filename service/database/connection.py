from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..settings import CONNECTION


bind = create_async_engine(url=CONNECTION, echo=True)
AsyncSessionLocal = async_sessionmaker(bind, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session