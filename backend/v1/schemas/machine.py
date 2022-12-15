from uuid import UUID

from pydantic import BaseModel


class MachineBase(BaseModel):
    id: UUID
    score: float


class MachineWrite(MachineBase):
    pass
