from pydantic import BaseModel

class OrgSubscIn(BaseModel):
    #id: str
    organization_tin: str
    subscription_name: str
    #is_active: bool

class OrgSubscOut(OrgSubscIn):
    """
    fields:
        id: int
        organization_tin: str
        subscription_name: str
        is_active: bool
    """
    id: int
    is_active: bool
