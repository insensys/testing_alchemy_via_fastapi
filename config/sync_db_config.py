from config.database_config import db_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SYNC_DB_URL=db_settings.get_postgres_url
engine = create_engine(SYNC_DB_URL)

SessionLocal = sessionmaker(bind=engine)