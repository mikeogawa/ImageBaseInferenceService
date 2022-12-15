from typing import Any, Dict, Optional

from fastapi.exceptions import HTTPException
from fastapi.security.api_key import APIKey
from fastapi.security.base import SecurityBase
from settings.const import MACHINEAUTH
from settings.db import Base, SessionDB
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR


class IsMachine:
    pass


def validate_authorization(authorization, auto_error):
    if not authorization:
        if auto_error:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
            )


def check_authorize(header_value: str, api_key: str) -> Dict[str, Any]:

    if header_value != api_key:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error (123)"
        )


class MachineAuth(SecurityBase):
    def __init__(
        self,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: Optional[bool] = True
    ):
        self.model = APIKey(**{"name": MACHINEAUTH.API_HEADER, "in": "header", "description": description})
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    def get_user_model(self, app_meta: Dict[str, Any]) -> Base:

        sub_id = app_meta.get("sub_id")
        if sub_id is None:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error (222)"
            )

        with SessionContext() as db:
            return db.query(self.base_model).get(self.base_model.sub_id == sub_id)

    def __call__(self, request: Request) -> Optional[IsMachine]:
        authorization: str = request.headers.get(MACHINEAUTH.API_HEADER)
        auto_error = self.auto_error
        validate_authorization(authorization, auto_error)

        if not authorization and not auto_error:
            return None

        check_authorize(authorization, MACHINEAUTH.API_KEY)

        return IsMachine()


machine_auth = MachineAuth(
    "Machine API Key",
    "Insert Patient Auth Key",
    True,
)
