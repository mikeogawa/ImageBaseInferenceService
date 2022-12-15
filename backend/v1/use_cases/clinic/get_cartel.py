from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.orm import Session
from utils import logging
from v1.models import Doctor as DoctorModel
from v1.service import ClinicCartelService

logger = logging.getLogger(__name__)


@dataclass
class GetCartel:
    db: Session

    def execute(self, doctor: DoctorModel, cartel_id: UUID):
        logger.info("get cartel doctor_id: %s, cartel_id: %s", doctor.id, cartel_id)

        cartel_service = ClinicCartelService(self.db)
        return cartel_service.get(doctor.clinic_id, cartel_id)
