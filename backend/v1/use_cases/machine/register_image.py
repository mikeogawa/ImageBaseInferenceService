from dataclasses import dataclass
from typing import Any, Dict

from fastapi import File
from sqlalchemy.orm import Session
from utils import logging
from v1.domain import MachineImage
from v1.models import Image as ImageModel
from v1.repositories import BasePatientRepository
from v1.service import MachineImageService

logger = logging.getLogger(__name__)


@dataclass
class RegiserImage:
    db: Session
    patient_repository: BasePatientRepository

    def execute(self, payload: Dict[str, Any], file: File):
        logger.info("payload", payload)
        cartel_service = MachineImageService(
            self.db,
            patient_repository=self.patient_repository,
        )
        machine_image: MachineImage = cartel_service.make_entity(payload)
        image_model: ImageModel = cartel_service.create(machine_image)
        machine_image.update_id(image_model.id)
        machine_image.update_image(file)
        cartel_service.update_s3_url(image_model, machine_image)
        self.db.commit()
