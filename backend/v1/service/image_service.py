from dataclasses import dataclass
from typing import Any, Dict, Optional
from uuid import UUID

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Query, Session
from starlette.status import HTTP_400_BAD_REQUEST
from utils.dict2obj import Dict2Obj
from v1.domain import ClinicImage, MachineImage
from v1.models import Cartel as CartelModel
from v1.models import Clinic as ClinicModel
from v1.models import Image as ImageModel
from v1.repositories import BaseAnalyzeRepostiory, BasePatientRepository


@dataclass
class ImageService:
    db: Session

    @property
    def query(self) -> Query:
        return self.db.query(ImageModel)

    @property
    def clinic_query(self) -> Query:
        return self.db.query(ClinicModel)

    @property
    def cartel_query(self) -> Query:
        return self.db.query(CartelModel)

    def validate_cartel(self, clinic_id: UUID, cartel_id: UUID):
        cartel = self.cartel_query.filter_by(id=cartel_id, clinic_id=clinic_id)
        if not cartel:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Cartel Not Found")


@dataclass
class ClinicImageService(ImageService):
    analyze_repoitory: Optional[BaseAnalyzeRepostiory] = None

    def list(self, cartel_id: UUID) -> list[ClinicImage]:
        image_list = self.query.filter_by(cartel_id=str(cartel_id)).all()
        res = []
        for image in image_list:
            res.append(
                ClinicImage(
                    id=str(image.id),
                    s3_url=image.s3_url,
                    score=image.score,
                    is_analyzing=image.is_analyzing,
                    cartel_id=str(image.cartel_id),
                    analyze_repoitory=self.analyze_repoitory,
                )
            )
        return res

    def get(self, cartel_id: UUID, id_: UUID) -> ClinicImage:
        image = self.query.filter_by(cartel_id=str(cartel_id), id=str(id_)).first()
        if not image:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Image Not Found")

        return ClinicImage(
            id=image.id,
            s3_url=image.s3_url,
            score=image.score,
            is_analyzing=image.is_analyzing,
            cartel_id=str(image.cartel_id),
            analyze_repoitory=self.analyze_repoitory,
        )

    def set_image_running(self, cartel_id: UUID, id_: UUID):
        image = self.query.filter_by(cartel_id=str(cartel_id), id=str(id_)).first()
        if not image:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Image Not Found")
        image.is_analyzing = True


@dataclass
class MachineImageService(ImageService):
    patient_repository: Optional[BasePatientRepository] = None
    analyze_repoitory: Optional[BaseAnalyzeRepostiory] = None

    def make_entity(self, payload: Dict[str, Any]) -> MachineImage:
        image: MachineImage = Dict2Obj(payload).convert_to(
            MachineImage,
            patient_repository=self.patient_repository,
        )
        return image

    def create(self, image: MachineImage) -> ImageModel:
        item = ImageModel(
            cartel_id=str(image.cartel_id),
        )
        self.db.add(item)
        self.db.flush()
        self.db.refresh(item)
        return item

    def update_s3_url(self, image_model: ImageModel, image: MachineImage):
        image_model.s3_url = image.s3_url
        self.db.add(image_model)
        self.db.flush()

    def update_score(self, id_: UUID, score: float):
        image = self.query.filter_by(id=id_).first()
        image.score = score
        image.is_analyzing = False
        self.db.flush()
