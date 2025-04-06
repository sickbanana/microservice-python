from asyncio import get_event_loop_policy
import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from ..settings import TEST_CONNECTION
from ..database.connection import get_session
from ..database.models import Base
from ..main import app

bind = create_async_engine(url=TEST_CONNECTION)
AsyncSessionLocal = async_sessionmaker(bind, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(scope="session")
def event_loop():
    loop = get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def get_client():
    async def override_get_db() -> AsyncSession:
        async with AsyncSessionLocal() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


@pytest_asyncio.fixture(scope="function", autouse=True)
async def create_tables():
    async with bind.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture(scope="function")
async def get_test_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
