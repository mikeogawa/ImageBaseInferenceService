import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CartelBase(BaseModel):
    diagnosis: str
    prescription: str
    doctor_id: Optional[UUID]


class CartelRead(CartelBase):
    id: UUID
    date: datetime.datetime
    summary: str
    symptom: str
    paint_point: str
    tempreture: str
    pain_start: str
    pain_end: str
    prior_prescription: str
    allergy: str
    prior_issues: str
    user_id: str


class CartelWrite(CartelBase):
    pass
