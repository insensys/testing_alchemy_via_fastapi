from starlette_admin.auth import AdminUser, AuthProvider
from sqlalchemy.ext.asyncio import create_async_engine
from starlette_admin.contrib.sqla import Admin, ModelView
from .ad_views.org_view import OrganizationView
from .ad_views.subcription_view import SubscriptionView
from .ad_views.org_subc_view import OrganizationSubscriptionView
from models_folder.models import Organization, Subscription, OrganizationSubscription
from models_folder.app_user import AppUser
from .ad_views.app_user_view import AppUserView
from .ad_auth import SimpleAuthProvider
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware import Middleware
from config.sync_db_config import engine


admin = Admin(
    engine,
    auth_provider = SimpleAuthProvider(),
    middlewares= [Middleware(SessionMiddleware, secret_key="This temp secret key")],
    )


admin.add_view(OrganizationView(Organization))
admin.add_view(SubscriptionView(Subscription))
admin.add_view(OrganizationSubscriptionView(OrganizationSubscription))
admin.add_view(AppUserView(AppUser))