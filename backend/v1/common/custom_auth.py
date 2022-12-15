import json
from typing import Any, Dict, Optional, Type

import jwt
import requests
from fastapi.exceptions import HTTPException
from fastapi.security.api_key import APIKey
from fastapi.security.base import SecurityBase
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR

from settings.const import ENV, JWT
from settings.db import Base, SessionDB
from v1.models import Clinic, Patient


def get_public_key(token) -> str:

    if ENV == "local":
        return JWT.LOCAL_SECRET

    header = jwt.get_unverified_header(token)
    jwks = requests.get(
        'https://{}/.well-known/jwks.json'.format(JWT.END_POINT).json()
    )
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            return jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))


def validate_authorization(authorization, auto_error):
    if not authorization:
        if auto_error:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
            )


def jwt_decode_token(token: str) -> Dict[str, Any]:

    if not JWT.VERIFICATION:
        return jwt.decode(token, algorithms=JWT.ALGORITHM, options={"verify_signature": False})

    public_key = get_public_key(token)

    if public_key is None:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error (123)"
        )

    issuer = 'https://{}/'.format(JWT.END_POINT)
    return jwt.decode(token, public_key, audience=JWT.AUDIENCE, issuer=issuer, algorithms=JWT.ALGORITHM, options={"verify_signature": True})


class CustomAuth(SecurityBase):
    def __init__(
        self,
        base_model: Type[Base],
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: Optional[bool] = True
    ):
        self.model = APIKey(**{"name": JWT.AUTHENTICATION_KEY, "in": "header", "description": description})
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error
        self.base_model = base_model

    def get_user_model(self, app_meta: Dict[str, Any]) -> Base:

        sub_id = app_meta.get("sub_id")
        if sub_id is None:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error (222)"
            )

        with SessionDB() as db:
            return db.query(self.base_model).get(self.base_model.sub_id == sub_id)

    def __call__(self, request: Request) -> Optional[Base]:
        authorization: str = request.headers.get(JWT.AUTHENTICATION_KEY)
        auto_error = self.auto_error
        validate_authorization(authorization, auto_error)

        if not authorization and not auto_error:
            return None

        payload = jwt_decode_token(authorization)
        app_meta = payload["app_meta"]
        return self.get_user_model(app_meta)


patient_auth = CustomAuth(
    Patient,
    "Patient API Key",
    "Insert Patient Auth Key",
    True,
)

clinic_auth = CustomAuth(
    Clinic,
    "Clinic API Key",
    "Insert Clinic Auth Key",
    True,
)
