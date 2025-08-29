from __future__ import annotations
from datetime import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
import sqlalchemy as sa
from .models import Base


class AppUser(Base):
    __tablename__ = 'app_user'

    user_inn: Mapped[str]=mapped_column(sa.String(50), primary_key=True )
    email: Mapped[str]=mapped_column(sa.String(50), unique=True, nullable=False)
    password: Mapped[str]=mapped_column(sa.String(255))
    user_name: Mapped[str]=mapped_column(sa.String(35))
    created_at: Mapped[datetime]=mapped_column(sa.DateTime)

    organizations: Mapped[List["Organization"]]=relationship("Organization", back_populates="app_users")
