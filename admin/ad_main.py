from starlette_admin.auth import AdminUser, AuthProvider
from sqlalchemy import create_engine
from starlette_admin.contrib.sqla import Admin, ModelView
from config.database_config import db_settings
from models import Organization, Subscription, OrganizationSubscription, OrganizationView
from fastapi import FastAPI



engine = create_engine(db_settings.DB_URL, connect_args={"check_same_thread":False})
admin = Admin(engine)
app = FastAPI()
admin.add_view(ModelView(OrganizationView))
admin.add_view(ModelView(Subscription))
admin.add_view(ModelView(OrganizationSubscription))

admin.mount_to(app)