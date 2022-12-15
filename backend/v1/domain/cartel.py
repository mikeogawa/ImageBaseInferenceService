import datetime
from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class ClinicReadCartelPatient:
    id: str
    first_name: str
    last_name: str


@dataclass
class ClinicReadCartel:
    id: str
    date: datetime.datetime
    symptom: str
    prescription: str
    paint_point: str
    tempreture: float
    pain_start: Optional[datetime.datetime]
    pain_end: Optional[datetime.datetime]
    prior_prescription: str
    allergy: str
    prior_issues: str
    diagnosis: str
    prescription: str
    patient: ClinicReadCartelPatient
    patient_id: str
    doctor_id: Optional[UUID] = None
    images: Optional[list[UUID]] = None


@dataclass
class ClinicUpdateCartel:
    doctor_id: UUID
    diagnosis: str
    prescription: str
