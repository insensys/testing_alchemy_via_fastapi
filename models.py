from sqlalchemy import String, Text, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Organization(Base):
    __tablename__ = "organization"

    legal_person_tin: Mapped[str] = mapped_column(String(255), primary_key=True, unique=True)
    organization_name: Mapped[str] = mapped_column(String(255))

    org_subscription: Mapped[list["OrganizationSubscription"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    

class Subscription(Base):
    __tablename__ = "subscription"

    name: Mapped[str] = mapped_column(String(150), primary_key=True)
    description: Mapped[str] = mapped_column(Text)

    organizations_on_this_subs: Mapped[list["OrganizationSubscription"]] = relationship(
        back_populates="subscription",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class OrganizationSubscription(Base):
    """
    fields to add:
        organization_tin:str
        subscription_name:str
    """
    __tablename__ = "organization_subscription"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_tin: Mapped[str] = mapped_column(ForeignKey("organization.legal_person_tin"))
    subscription_name: Mapped[str] = mapped_column(ForeignKey("subscription.name"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    organization: Mapped["Organization"] = relationship(back_populates="org_subscription")
    subscription: Mapped["Subscription"] = relationship(back_populates="organizations_on_this_subs") 


