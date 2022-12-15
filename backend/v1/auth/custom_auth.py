import json
from typing import Any, Dict, Optional, Type

import jwt
import requests
from fastapi.exceptions import HTTPException
from fastapi.security.api_key import APIKey
from fastapi.security.base import SecurityBase
from settings.const import ENV, JWT
from settings.db import Base, SessionContext
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR
from v1.models import Doctor, Patient


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

    issuer = JWT.END_POINT
    return jwt.decode(token, public_key, audience=JWT.AUDIENCE, issuer=issuer, algorithms=JWT.ALGORITHM, options={"verify_signature": True})


class CustomAuth(SecurityBase):
    def __init__(
        self,
        base_model: Type[Base],
        authentication_key: str,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: Optional[bool] = True
    ):
        self.model = APIKey(**{"name": authentication_key, "in": "header", "description": description})
        self.authentication_key = authentication_key
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error
        self.base_model = base_model

    def get_user_model(self, sub_id: str, app_meta: Dict[str, Any]) -> Base:

        type_user = app_meta.get("type")
        if type_user is None:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error (222): User Type"
            )

        with SessionContext() as db:
            return db.query(self.base_model).filter(self.base_model.sub_id == sub_id).first()

    def __call__(self, request: Request) -> Optional[Base]:
        authorization: str = request.headers.get(self.authentication_key)
        auto_error = self.auto_error
        validate_authorization(authorization, auto_error)

        if not authorization and not auto_error:
            return None

        payload = jwt_decode_token(authorization)
        sub_id = payload["sub"]
        app_meta = payload["app_meta"]

        return self.get_user_model(sub_id, app_meta)


clinic_auth = CustomAuth(
    Doctor,
    JWT.AUTHENTICATION_KEY,
    "Clinic API Key",
    "Insert Clinic Auth Key",
    True,
)
patient_auth = CustomAuth(
    Patient,
    JWT.AUTHENTICATION_KEY_2,
    "Patient API Key",
    "Insert Patient Auth Key",
    True,
)
