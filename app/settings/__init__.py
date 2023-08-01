from pydantic_settings import BaseSettings

from app.settings.db import DBSettings


class AppSettings(BaseSettings):
    db: DBSettings = DBSettings()

