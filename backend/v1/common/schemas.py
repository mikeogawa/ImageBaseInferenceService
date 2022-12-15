from pydantic import BaseModel


class StatusOk(BaseModel):
    status: str = "200"
    detail: str = "OK"
