from fastapi import APIRouter, Depends
from typing import List
from schemas import SubscriptionCreateOut
from db_config import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from service_folder.subdscription_service import get_all_subscriptions


subscription_router = APIRouter(
    prefix="/subscription",
    tags= ["subscriptions"] #TODO: узнать подробнее об этой фиче зачем она нужна
)

@subscription_router.get("/get_list", response_model= List[SubscriptionCreateOut])
async def get_list_subscription(db_connection: AsyncSession=Depends(get_async_session)):
    return await get_all_subscriptions(db_connection)