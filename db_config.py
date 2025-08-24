from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from models import Base

DB_URL = "sqlite+aiosqlite:///./experimental.db"
engine = create_async_engine(DB_URL, echo = True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit= False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    try:
        async with AsyncSessionLocal() as session:
            yield session
    finally:
        await session.close()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)