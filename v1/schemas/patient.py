from pydantic import BaseModel


class PatientBase(BaseModel):
    sub_id: str


class PatientRead(PatientBase):
    id: str
    first_name: str
    last_name: str
