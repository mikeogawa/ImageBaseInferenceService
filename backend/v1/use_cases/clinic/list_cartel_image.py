from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.orm import Session
from utils import logging
from v1.models import Doctor as DoctorModel
from v1.service import ClinicImageService

logger = logging.getLogger(__name__)


@dataclass
class ListCartelImage:
    db: Session

    def execute(self, doctor: DoctorModel, cartel_id: UUID):
        logger.info("get cartel doctor_id: %s, cartel_id: %s", doctor.id, cartel_id)

        cartel_service = ClinicImageService(self.db)
        cartel_service.validate_cartel(doctor.clinic_id, cartel_id)
        return cartel_service.list(cartel_id)
