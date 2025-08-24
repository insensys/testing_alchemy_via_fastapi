from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import  HTTPException
from sqlalchemy import select
from models import Subscription
from schemas import SubscriptionCreateOut
from typing import List

async def get_all_subscriptions( db_connection: AsyncSession) -> List[SubscriptionCreateOut]:
    """
    Gets all subscription list from DB
    """
    
    try:
        sql_statement = select(Subscription)
        query_result = await db_connection.execute(sql_statement)
        list_subscriptions = query_result.scalars().all()
        count:int = 1
        for sub in list_subscriptions:
            print (count)
            print (sub.name)
            print (sub.description)
            count+=1

        susbcription_list=[
            SubscriptionCreateOut.model_validate(subscription)
            for subscription in list_subscriptions
        ]
        return susbcription_list
    
    except Exception as e:
        await db_connection.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error getting list of subsciption: {str(e)}"
        )