# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import mlflow
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from errors.http_errors import http_error_handler
from errors.validation_errors import http422_error_handler
from routes.home_router import app as home_router
from config.project_config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION, DEBUG, PROJECT_NAME
from events.server_events import create_start_app_handler, create_stop_app_handler
def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup", create_start_app_handler(application))
    application.add_event_handler(
        "shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(
        RequestValidationError, http422_error_handler)

    application.include_router(home_router, prefix=API_PREFIX)
    return application


app = get_application()

@app.get("/")
async def root():
    return {"message": "App Running!"}