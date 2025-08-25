from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from models import Base
from config.database_config import db_settings
from sqlalchemy import text




DB_URL = db_settings.DB_URL
#DB_URL = "postgresql+asyncpg://localhost_user:1234@localhost:5432/experimental"
engine = create_async_engine(DB_URL, echo = True, pool_pre_ping=True)
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
