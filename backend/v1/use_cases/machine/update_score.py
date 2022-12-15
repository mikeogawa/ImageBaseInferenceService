from dataclasses import dataclass
from typing import Any, Dict

from sqlalchemy.orm import Session

from v1.repositories import BaseAnalyzeRepostiory
from v1.service import MachineImageService
from v1.utils import logging

logger = logging.getLogger(__name__)


@dataclass
class UpdateScore:
    db: Session
    analyze_repository: BaseAnalyzeRepostiory

    def execute(self, payload: Dict[str, Any]):
        logger.info("payload", payload)
        cartel_service = MachineImageService(
            self.db,
            analyze_repoitory=self.analyze_repository,
        )
        cartel_service.update_score(payload["id"], payload["score"])
        self.db.commit()
