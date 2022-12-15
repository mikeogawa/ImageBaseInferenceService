from dataclasses import dataclass
from typing import Any, Dict

from sqlalchemy.orm import Session

from v1.models import Doctor as DoctorModel
from v1.repositories import BaseAnalyzeRepostiory
from v1.service import ClinicImageService
from v1.utils import logging

logger = logging.getLogger(__name__)


@dataclass
class ReAnalyze:
    db: Session
    analyze_repostiory: BaseAnalyzeRepostiory

    def execute(self, doctor: DoctorModel, payload: Dict[str, Any]):
        logger.info("update doctor: %s payload: %s", doctor.id, payload)

        image_id = payload["image_id"]
        cartel_id = payload["cartel_id"]

        clinic_service = ClinicImageService(self.db)
        clinic_service.validate_cartel(doctor.clinic_id, cartel_id)
        image = clinic_service.get(cartel_id, image_id)
        image.reanalyze()
        clinic_service.set_image_running(cartel_id, image_id)
