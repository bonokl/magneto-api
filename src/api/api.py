import time
from contextlib import asynccontextmanager
from http import HTTPStatus
from typing import Callable

from fastapi import APIRouter, FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from src import variables
from src.api import design_api, functions_api, magnet_materials_api, magnets_api, simulations_api
from src.api.docs import get_redoc_documentation, get_swagger_documentation, openapi
from src.api.healthcheck import healthcheck
from src.entities.design import Design
from src.entities.function import Function
from src.entities.magnet import Magnet
from src.entities.magnet_material import MagnetMaterial, MaterialGrade
from src.entities.pagination import Paginated
from src.logger import logger


class API:
    app: FastAPI
    _origins: list = [
        "http://localhost",
        "http://localhost:8080",
    ]

    @classmethod
    def initialize(cls) -> FastAPI:
        cls.app = FastAPI(
            title="Magneto",
            summary="Magneto API",
            version="1.0.0",
            docs_url=None,
            redoc_url=None,
            openapi_url=None,
            lifespan=lifespan,
        )

        cls._add_middlewares()
        cls._register_exception_handlers()
        cls._register_routes()

        return cls.app

    @classmethod
    def _add_middlewares(cls):
        cls.app.add_middleware(LogRequestsMiddleware)
        cls.app.add_middleware(
            CORSMiddleware,
            allow_origins=cls._origins,
            allow_credentials=True,
            allow_methods=["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"],
            allow_headers=["*"],
        )

    @classmethod
    def _register_exception_handlers(cls):
        @cls.app.exception_handler(HTTPException)
        async def auth_exception_handler(request: Request, exc: HTTPException):
            return JSONResponse(
                status_code=exc.status_code,
                headers=exc.headers,
                content=jsonable_encoder({"message": exc.detail}),
            )

        @cls.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc: RequestValidationError):
            return JSONResponse(
                content=jsonable_encoder({"message": exc.errors()}),
                status_code=status.HTTP_400_BAD_REQUEST
            )

        @cls.app.exception_handler(Exception)
        async def base_exception_handler(request: Request, exc: Exception):
            message = getattr(exc, "message", "system error occurred")
            logger.exception(message)

            status_code = getattr(exc, "status_code", status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JSONResponse(
                content=jsonable_encoder({
                    "message": message,
                }),
                status_code=status_code
            )

    @classmethod
    def _register_routes(cls) -> None:
        cls._router = APIRouter()

        cls._router.add_api_route("/health", healthcheck, methods=["GET"], tags=["Health Check"])

        cls._router.prefix = f"{variables.base_url}"

        cls._add_docs_routes()

        ########################
        # Functions
        ########################
        cls._add_route("/functions", functions_api.get_all_functions, ["GET"], tags=["Functions"],
                       response_model=Paginated[Function])
        cls._add_route("/functions/{function_id:str}", functions_api.get_function, ["GET"], tags=["Functions"],
                       response_model=Function)

        ########################
        # Magnets
        ########################
        cls._add_route("/magnets", magnets_api.get_all_magnets, ["GET"], tags=["Magnets"],
                       response_model=Paginated[Magnet])
        cls._add_route("/magnets/{magnet_id:str}", magnets_api.get_magnet, ["GET"], tags=["Magnets"],
                       response_model=Magnet)

        ########################
        # Magnet Materials
        ########################
        cls._add_route("/magnet-materials", magnet_materials_api.get_all_magnet_materials, ["GET"],
                       tags=["MagnetMaterials"],
                       response_model=Paginated[MagnetMaterial])
        cls._add_route("/magnet-materials/{material_id:int}/grades", magnet_materials_api.get_all_material_grades,
                       ["GET"], tags=["MagnetMaterials"],
                       response_model=Paginated[MaterialGrade])

        ########################
        # Designs
        ########################
        cls._add_route("/designs", design_api.get_all_designs, ["GET"], tags=["Designs"],
                       response_model=Paginated[Design])
        cls._add_route("/designs/{design_id:int}", design_api.get_design, ["GET"], tags=["Designs"],
                       response_model=Design)
        cls._add_route("/designs", design_api.create_design, ["POST"], tags=["Designs"],
                       response_model=Design)
        cls._add_route("/designs/{design_id:int}", design_api.update_design, ["PUT"], tags=["Designs"],
                       response_model=Design)
        cls._add_route("/designs/{design_id:int}", design_api.delete_design, ["DELETE"], tags=["Designs"])

        ########################
        # Designs
        ########################
        cls._add_route("/simulations/{design_id:int}/simulate", simulations_api.simulate, ["POST"],
                       tags=["Simulations"],
                       response_model=list)

        cls.app.include_router(cls._router)

    @classmethod
    def _add_route(cls, path: str, func: Callable, methods: list[str], tags: list[str] = None, **kwargs):
        cls._router.add_api_route(path, func, methods=methods, tags=tags, **kwargs)

    @classmethod
    def _add_docs_routes(cls):
        cls._router.add_api_route("/docs", get_swagger_documentation, methods=["GET"], include_in_schema=False)
        cls._router.add_api_route("/redoc", get_redoc_documentation, methods=["GET"], include_in_schema=False)
        cls._router.add_api_route("/openapi.json", openapi(cls.app), methods=["GET"], include_in_schema=False)


class LogRequestsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time: float = time.time()
        response = await call_next(request)
        end_time: float = time.time()
        elapsed_time: float = end_time - start_time
        logger.info(
            f"{request.method} {request.url} \"{request.scope.get("scheme", "").upper()}/"
            f"{request.scope.get("http_version")} {response.status_code} {HTTPStatus(response.status_code).phrase}\" "
            f"{elapsed_time:.2f}s"
        )
        return response


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
