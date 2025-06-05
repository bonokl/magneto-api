import secrets
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src import variables

security = HTTPBasic()


def validate_docs_access(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    correct_username = secrets.compare_digest(credentials.username, variables.docs_user)
    correct_password = secrets.compare_digest(credentials.password, variables.docs_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


async def get_swagger_documentation(username: str = Depends(validate_docs_access)):
    return get_swagger_ui_html(openapi_url=f"{variables.base_url}/openapi.json", title="docs")


async def get_redoc_documentation(username: str = Depends(validate_docs_access)):
    return get_redoc_html(openapi_url=f"{variables.base_url}/openapi.json", title="docs")


def openapi(app: FastAPI):
    async def fun(username: str = Depends(validate_docs_access)):
        return get_openapi(title=app.title, version=app.version, routes=app.routes)

    return fun
