from fastapi import Depends, FastAPI
from typing import Annotated

from config import get_app_settings
from routers import employee_router_v1
from settings import AppSettings


def create_app():
    app = FastAPI(openapi_prefix='/dev')
    app.include_router(employee_router_v1, prefix='/v1')

    @app.get('/status')
    async def status():
        """
        Display the status of the API.
        """
        return {'message': 'I am healthy'}

    @app.get('/region')
    async def region(settings: Annotated[AppSettings, Depends(get_app_settings)]):
        """
        Display the region where the database used in the API is deployed.
        """
        return settings.db.DB_REGION_NAME

    return app
