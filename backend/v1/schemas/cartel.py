import datetime
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


class CartelBase(BaseModel):
    diagnosis: str
    prescription: str


class CartelRead(CartelBase):
    id: UUID
    date: datetime.datetime
    symptom: str
    paint_point: str
    tempreture: str
    pain_start: Optional[datetime.datetime]
    pain_end: Optional[datetime.datetime]
    prior_prescription: str
    allergy: str
    prior_issues: str
    patient_id: UUID
    doctor_id: Optional[UUID]


class CartelWrite(CartelBase):
    pass
