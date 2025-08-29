from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models_folder.models import Organization, Subscription
from schemas import (OrganizationCreateIn, OrganizationCreateOut,
                     SubscriptionCreateIn,
                     SubscriptionCreateOut)


async def add_organization(user_input_organization: OrganizationCreateIn, db: AsyncSession) -> OrganizationCreateOut:
    """
    Добавляет новую организацию в базу данных
    """
    try:
        # Создаем новый объект организации
        db_organization = Organization(
            legal_person_tin=user_input_organization.legal_person_tin,
            organization_name=user_input_organization.organization_name
        )
        
        # Добавляем в сессию и сохраняем
        db.add(db_organization)
        await db.commit()
        db.refresh(db_organization)
        
        return OrganizationCreateOut(
            legal_person_tin=db_organization.legal_person_tin,
            organization_name=db_organization.organization_name
        )
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Ошибка при добавлении организации: {str(e)}")


async def get_org_by_name(org_name:str, db: AsyncSession) -> OrganizationCreateOut:
    """
    Search org by name in DB
    """
    try:
        org_from_db = db.query(Organization).filter(
            Organization.organization_name.ilike(f"%{org_name}")
        ).first()

        if not org_from_db:
            raise HTTPException(status_code=404, detail="No organization")
        
        return OrganizationCreateOut(
            legal_person_tin=org_from_db.legal_person_tin,
            organization_name=org_from_db.organization_name
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=405,  detail=f"Eorrrrr")
    

async def create_subsc(user_input_subsc: SubscriptionCreateIn, open_db_session: AsyncSession) -> SubscriptionCreateOut:
    try:
        #query to db to find similar records
        stmt = select(Subscription).where(Subscription.name == user_input_subsc.name)
        #executing query
        result_query =  await open_db_session.execute(stmt)
        # desrializing 
        existing_record = result_query.scalar_one_or_none()

        #if exists then break
        if existing_record:
            raise ValueError(f"Такая запись существует: {existing_record.name}")
        
        # Создаем новый объект подписки
        added_subscription = Subscription(
            name=user_input_subsc.name,
            description=user_input_subsc.description,
        )

        # Добавляем объект в сессию (подготавливаем для сохранения)
        open_db_session.add(added_subscription)
        # Сохраняем изменения в базе данных
        await open_db_session.commit()
        # Обновляем объект данными из БД (получаем ID и другие авто-генерируемые поля)
        open_db_session.refresh(added_subscription)

        return SubscriptionCreateOut.model_validate(added_subscription)
    except Exception as e:
        raise HTTPException(status_code=410, detail=f"Error writing subscription: {str(e)}")