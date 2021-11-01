from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    print("exc.detail",exc.detail)
    return JSONResponse({"errors": exc.detail}, status_code=exc.status_code)