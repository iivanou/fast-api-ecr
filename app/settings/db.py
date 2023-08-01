from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_REGION_NAME: str
    DB_ACCESS_KEY_ID: str
    DB_SECRET_ACCESS_KEY: str

    class Config:
        env_file = ".env"
        extra = 'allow'
