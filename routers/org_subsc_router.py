from fastapi import APIRouter
from schemas_folder.org_subsc_schema import OrgSubsc


org_subsc_router = APIRouter(
    prefix="/org_subsc",
    tags=["Organization subscription", "Subscription"]
)

org_subsc_router.post("/add_new_org", response_model= OrgSubsc)