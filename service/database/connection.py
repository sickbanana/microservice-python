from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


bind = create_async_engine(f"postgresql+asyncpg://postgres:password@localhost/postgres", echo=True)
AsyncSessionLocal = async_sessionmaker(bind, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


