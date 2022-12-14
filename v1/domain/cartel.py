import datetime
from dataclasses import dataclass
from typing import Optional
from uuid import UUID


class ClinicReadCartelPatient:
    id: UUID
    firt_name: UUID
    last_name: UUID


@dataclass
class ClinicReadCartel:
    id: UUID
    date: datetime.datetime
    summary: str
    symptom: str
    prescription: str
    paint_point: str
    tempreture: float
    pain_start: datetime.datetime
    pain_end: datetime.datetime
    prior_prescription: str
    allergy: str
    prior_issues: str
    diagnosis: str
    prescription: str
    user: ClinicReadCartelPatient
    doctor_id: Optional[UUID] = None
    images: Optional[list[UUID]] = None


@dataclass
class ClinicUpdateCartel:
    doctor_id: UUID
    diagnosis: str
    prescription: str
