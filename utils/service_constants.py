from enum import Enum


class ConfigStrings(Enum):
    SYNC_POSTGRES="postgresql+psycopg2"
    ENV_NAME=".env"