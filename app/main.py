from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.api.routers import main_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)
app.include_router(main_router)


@app.exception_handler(HTTPException)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content=jsonable_encoder(
            dict(
                code=HTTPStatus.NOT_FOUND,
                message='Item not found',
            )
        )
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content=jsonable_encoder(
            dict(
                code=HTTPStatus.BAD_REQUEST,
                message='Validation Failed',
            )
        )
    )
