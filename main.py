from routers import healthcheck_router
from fastapi import FastAPI
from constants import IS_SWAGGER_ENABLED, SITE_TITLE

swagger_params = {}
if not IS_SWAGGER_ENABLED:
    swagger_params = {"openapi_url": None, "docs_url": None, "redoc_url": None}


app = FastAPI(title=SITE_TITLE, root_path=None, swagger_ui_parameters={"persistAuthorization": True}, **swagger_params)


app.include_router(healthcheck_router)