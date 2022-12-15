from uuid import UUID

from pydantic import BaseModel


class ClinicBase(BaseModel):
    name: str


class ClinicRead(ClinicBase):
    id: UUID


class ClinicWrite(ClinicBase):
    pass
