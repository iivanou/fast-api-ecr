import boto3
from boto3.resources.base import ServiceResource
from fastapi import Depends
from typing import Annotated

from app.settings import AppSettings
from app.config import get_app_settings


def db_connection(settings: Annotated[AppSettings, Depends(get_app_settings)]) -> ServiceResource:
    return boto3.resource(
        'dynamodb',
        region_name=settings.db.DB_REGION_NAME,
        aws_access_key_id=settings.db.DB_ACCESS_KEY_ID,
        aws_secret_access_key=settings.db.DB_SECRET_ACCESS_KEY
    )
