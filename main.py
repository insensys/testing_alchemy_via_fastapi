from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends
from models import Base, Subscription
from schemas import OrganizationCreateIn, OrganizationCreateOut, SubscriptionCreateOut, SubscriptionCreateIn
from services import add_organization, get_org_by_name, create_subsc
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from db_config import get_async_session, create_tables
from routers.subscription_router import subscription_router
from sqlalchemy.ext.asyncio import AsyncSession



# DB_URL_SYNC = "sqlite:///./experimental.db"
# engine = create_engine(DB_URL_SYNC, echo=True)
# Base.metadata.create_all(engine)





@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    # Base.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(subscription_router)

@app.get("/")
async def hello_func():
    return "Hello world"

@app.post("/add_organization", response_model=OrganizationCreateOut)
async def add_org(user_input_organization: OrganizationCreateIn, db: AsyncSession = Depends(get_async_session)):
    """
    Adding new organization in database
    """
    created_org = await add_organization(user_input_organization, db)
    return created_org


@app.get("/org_by_name", response_model=OrganizationCreateOut)
async def org_by_name(org_name: str, db: AsyncSession = Depends(get_async_session)):
    """
    Search in db
    """
    return await get_org_by_name(org_name, db)


@app.post("/add_subscription", response_model=SubscriptionCreateOut)
async def add_subscription(subscription: SubscriptionCreateIn, open_db_session: AsyncSession = Depends(get_async_session)):
   return await create_subsc(subscription, open_db_session)





    

