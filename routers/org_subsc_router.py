from fastapi import APIRouter
from schemas_folder.org_subsc_schema import OrgSubscOut, OrgSubscIn
from  fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db_config import get_async_session
from service_folder.subdscription_service import add_new_org_subsc


org_subsc_router = APIRouter(
    prefix="/org_subsc",
    tags=["Organization subscription"]
)

@org_subsc_router.post("/add_new_record", response_model= OrgSubscOut)
async def add_new_org(new_org_data: OrgSubscIn, db_session: AsyncSession = Depends(get_async_session)):
    return await add_new_org_subsc(new_org_data, db_session)