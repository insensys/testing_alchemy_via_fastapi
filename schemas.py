from pydantic import BaseModel


class OrganizationCreateIn(BaseModel):
    legal_person_tin: str
    organization_name: str

class OrganizationCreateOut(BaseModel):
    legal_person_tin: str
    organization_name: str


    class Config:
        from_attributes = True


class SubscriptionCreateIn(BaseModel):
    name: str
    description: str

class SubscriptionCreateOut(SubscriptionCreateIn):
    pass

    class Config:
        from_attributes = True