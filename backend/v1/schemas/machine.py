from pydantic import BaseModel


class MachineBase(BaseModel):
    id: str
    score: float


class MachineWrite(MachineBase):
    pass
