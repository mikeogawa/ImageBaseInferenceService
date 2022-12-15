import datetime

from pydantic import BaseModel


class QuestionnaireBase(BaseModel):
    date: datetime.datetime
    paint_point: str
    tempreture: float
    pain_start: datetime.datetime
    pain_end: datetime.datetime
    prior_prescription: str
    allergy: str
    prior_issues: str


class QuestionnaireWrite(QuestionnaireBase):
    pass
