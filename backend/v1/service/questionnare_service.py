from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.orm import Query, Session
from v1.domain import Questionnare
from v1.models import Cartel as CartelModel


@dataclass
class QuestionnareService:
    db: Session

    @property
    def query(self) -> Query:
        return self.db.query(CartelModel)

    def create(self, patient_id: UUID, questionnare: Questionnare):

        item = CartelModel(
            date=questionnare.date,
            symptom=questionnare.symptom,
            paint_point=questionnare.paint_point,
            tempreture=questionnare.tempreture,
            pain_start=questionnare.pain_start,
            pain_end=questionnare.pain_end,
            prior_prescription=questionnare.prior_prescription,
            allergy=questionnare.allergy,
            prior_issues=questionnare.prior_issues,
            patient_id=str(patient_id),
            clinic_id=str(questionnare.clinic_id),
        )
        self.db.add(item)
        self.db.flush()
