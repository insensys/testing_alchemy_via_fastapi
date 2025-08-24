from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabseSettings(BaseSettings):
    DB_URL: str

    model_config = SettingsConfigDict(
        env_file=(".env")
    )

db_settings = DatabseSettings()
