from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import  HTTPException
from sqlalchemy import select
from models import Subscription
from schemas import SubscriptionCreateOut
from typing import List
from models import OrganizationSubscription

from schemas_folder.org_subsc_schema import OrgSubscIn, OrgSubscOut


async def get_all_subscriptions( db_connection: AsyncSession) -> List[SubscriptionCreateOut]:
    """
    Gets all subscription list from DB
    """
    
    try:
        sql_statement = select(Subscription)
        query_result = await db_connection.execute(sql_statement)
        list_subscriptions = query_result.scalars().all()

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

async def add_new_org_subsc(new_org_subsc_data: OrgSubscIn, db_session: AsyncSession) -> OrgSubscOut:
    """
    Adding new org subscription in database
    """

    try:
        parsed_data = OrganizationSubscription(
            organization_tin = new_org_subsc_data.organization_tin,
            subscription_name = new_org_subsc_data.subscription_name
        )

        db_session.add(parsed_data)

        await db_session.commit()
        await db_session.refresh(parsed_data)

        return OrgSubscOut(
        id = parsed_data.id,
        organization_tin = parsed_data.organization_tin,
        subscription_name = parsed_data.subscription_name,
        is_active = parsed_data.is_active
    )
    except Exception as e:
        await db_session.rollback()
        HTTPException(status_code=400, detail=f"Error after try to write in org_subsc table. More details:{e}")

    
    