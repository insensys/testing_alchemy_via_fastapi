from starlette_admin.auth import AdminUser, AuthProvider
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from starlette_admin.contrib.sqla import Admin, ModelView
from config.database_config import db_settings
from models import Organization, Subscription, OrganizationSubscription, OrganizationView, SubscriptionView, OrganizationSubscriptionView
import os

DB_URL = "postgresql+psycopg2://localhost_user:1234@localhost:5432/experimental"
engine = create_engine(DB_URL)


admin = Admin(engine)


admin.add_view(OrganizationView(Organization))
admin.add_view(SubscriptionView(Subscription))
admin.add_view(OrganizationSubscriptionView(OrganizationSubscription))