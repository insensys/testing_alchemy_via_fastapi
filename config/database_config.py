from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseSettings):
    DB_URL: str

    model_config = SettingsConfigDict(
        env_file=(".env"),
        extra="ignore"
    )

db_settings = DatabaseSettings()
