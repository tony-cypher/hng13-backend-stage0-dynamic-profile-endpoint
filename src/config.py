from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CONTACT_EMAIL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
