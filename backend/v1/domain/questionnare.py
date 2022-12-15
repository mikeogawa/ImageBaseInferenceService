import datetime
from dataclasses import dataclass


@dataclass
class Questionnare:
    date: datetime.datetime
    symptom: str
    paint_point: str
    tempreture: float
    pain_start: datetime.datetime
    pain_end: datetime.datetime
    prior_prescription: str
    allergy: str
    prior_issues: str
