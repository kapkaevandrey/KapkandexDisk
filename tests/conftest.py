import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

try:
    from app.core.db import get_async_session
    from app.core.base import Base
except (NameError, ImportError):
    raise AssertionError(
        'Not found object Base or generator get_async_session',
    )

try:
    from app.main import app
except (NameError, ImportError):
    raise AssertionError(
        'Dont find application "app"`.',
    )


pytest_plugins = [
    'tests.fixtures.items',
    'tests.fixtures.date',
    'tests.fixtures.response_body'
]


SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./test.db'


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    class_=AsyncSession, autocommit=False, autoflush=False, bind=engine,
)


async def override_db():
    async with TestingSessionLocal() as session:
        yield session


@pytest_asyncio.fixture(autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
async def session():
    async with TestingSessionLocal() as session:
        yield session
