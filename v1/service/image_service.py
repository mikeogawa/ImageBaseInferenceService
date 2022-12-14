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
    analyze_repoitory: BaseAnalyzeRepostiory

    def list(self, cartel_id: UUID) -> list[ClinicImage]:
        image_list = self.query.filter_by(cartel_id=cartel_id).all()
        res = []
        for image in image_list:
            res.append(
                ClinicImage(
                    id=image.id,
                    s3_url=image.s3_url,
                    score=image.score,
                    cartel_id=image.cartel_id,
                    user_id=image.user_id,
                    analyze_repoitory=self.analyze_repoitory,
                )
            )
        return res

    def get(self, cartel_id: str, id_: str) -> ClinicImage:
        image = self.query.filter_by(cartel_id=cartel_id, id=id_).first()
        if not image:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Image Not Found")

        return ClinicImage(
            id=image.id,
            s3_url=image.s3_url,
            score=image.score,
            cartel_id=image.cartel_id,
            user_id=image.user_id,
            analyze_repoitory=self.analyze_repoitory,
        )

    def set_image_running(self, cartel_id: str, id_: str):
        image = self.query.filter_by(cartel_id=cartel_id, id=id_).first()
        if not image:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Image Not Found")
        image.is_analyzing = True
        self.query.commit()
        self.query.flush()


@dataclass
class MachineImageService(ImageService):
    patient_repostiory: Optional[BasePatientRepository] = None
    analyze_repoitory: Optional[BaseAnalyzeRepostiory] = None

    def make_entity(self, payload: Dict[str, Any]) -> MachineImage:
        image: MachineImage = Dict2Obj(payload).convert_to(
            MachineImage,
            patient_repostiory=self.patient_repostiory,
        )
        return image

    def create(self, image: MachineImage) -> ImageModel:
        item = ImageModel(
            cartel_id=image.cartel_id,
            user_id=image.user_id,
            patient_repostiory=self.patient_repostiory,
            analyze_repoitory=self.analyze_repoitory,
        )
        self.query.add(item)
        self.query.commit()
        self.query.flush()
        return item

    def update_s3_url(self, image_model: ImageModel, image: MachineImage):
        image_model.s3_url = image.s3_url
        self.query.add(image_model)
        self.query.commit()
        self.query.flush()

    def update_score(self, id_: UUID, score: float):
        image = self.query.filter_by(id=id_).first()
        image.score = score
        image.is_analyzing = False
        self.query.commit()
        self.query.flush()
