import datetime
from uuid import UUID

from pydantic import BaseModel


class QuestionnaireBase(BaseModel):
    date: datetime.datetime
    symptom: str
    paint_point: str
    tempreture: float
    pain_start: datetime.datetime
    pain_end: datetime.datetime
    prior_prescription: str
    allergy: str
    prior_issues: str
    clinic_id: UUID


class QuestionnaireWrite(QuestionnaireBase):
    pass
