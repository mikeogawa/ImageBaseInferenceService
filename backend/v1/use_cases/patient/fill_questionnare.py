from dataclasses import dataclass
from typing import Any, Dict

from sqlalchemy.orm import Session
from utils import dict2obj, logging
from v1.domain import Questionnare
from v1.models import Patient as PatientModel
from v1.service import QuestionnareService

logger = logging.getLogger(__name__)


@dataclass
class FillQuestionnare:
    db: Session

    def execute(self, patient: PatientModel, payload: Dict[str, Any]):
        logger.info("payload", payload)
        questionnare: Questionnare = dict2obj.Dict2Obj(payload).convert_to(Questionnare)

        cartel_service = QuestionnareService(self.db)
        cartel_service.create(patient.id, questionnare)
        self.db.commit()
