from dataclasses import dataclass

from sqlalchemy.orm import Session

from v1.models import Doctor as DoctorModel
from v1.service import ClinicCartelService
from v1.utils import logging

logger = logging.getLogger(__name__)


@dataclass
class ListCartel:
    db: Session

    def execute(self, doctor: DoctorModel):
        logger.info("list %s", doctor.id)

        cartel_service = ClinicCartelService(self.db)
        return cartel_service.list(doctor.clinic_id)
