from pydantic import BaseModel


class PatientBase(BaseModel):
    id: str
    first_name: str
    last_name: str


class PatientRead(PatientBase):
    pass
