from starlette_admin.auth import AdminUser, AuthProvider
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from starlette_admin.contrib.sqla import Admin, ModelView
from config.database_config import db_settings
from db_config import DB_URL
from .ad_views.org_view import OrganizationView
from .ad_views.subcription_view import SubscriptionView
from .ad_views.org_subc_view import OrganizationSubscriptionView
from models_folder.models import Organization, Subscription, OrganizationSubscription
from models_folder.app_user import AppUser
from .ad_views.app_user_view import AppUserView


DB_URL=db_settings.get_postgres_url
engine = create_engine(DB_URL)


admin = Admin(engine)


admin.add_view(OrganizationView(Organization))
admin.add_view(SubscriptionView(Subscription))
admin.add_view(OrganizationSubscriptionView(OrganizationSubscription))
admin.add_view(AppUserView(AppUser))