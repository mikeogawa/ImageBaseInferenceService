from dataclasses import dataclass
from typing import Any, Dict

from sqlalchemy.orm import Session
from utils import logging
from v1.repositories import BaseAnalyzeRepostiory
from v1.service import MachineImageService

logger = logging.getLogger(__name__)


@dataclass
class UpdateScore:
    db: Session
    analyze_repository: BaseAnalyzeRepostiory

    def execute(self, payload: Dict[str, Any]):
        logger.info("payload %s", payload)
        cartel_service = MachineImageService(
            self.db,
            analyze_repoitory=self.analyze_repository,
        )
        cartel_service.update_score(payload["id"], payload["score"])
        self.db.commit()
