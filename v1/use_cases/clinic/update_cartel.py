from dataclasses import dataclass
from typing import Any, Dict
from uuid import UUID

from sqlalchemy.orm import Session

from v1.domain import ClinicUpdateCartel
from v1.models import Doctor as DoctorModel
from v1.service import ClinicCartelService
from v1.utils import dict2obj, logging

logger = logging.getLogger(__name__)


@dataclass
class UpdateCartel:
    db: Session

    def execute(self, doctor: DoctorModel, cartel_id: UUID, payload: Dict[str, Any]):
        payload["doctor"] = doctor.id
        logger.info("update doctor: %s payload: %s", doctor.id, payload)
        cartel = dict2obj.Dict2Obj(payload).convert_to(ClinicUpdateCartel)

        cartel_service = ClinicCartelService(self.db)
        cartel_service.update(doctor.clinic_id, cartel_id, cartel)
