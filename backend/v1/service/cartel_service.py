from dataclasses import dataclass
from uuid import UUID

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Query, Session
from starlette.status import HTTP_400_BAD_REQUEST
from v1.domain import (ClinicReadCartel, ClinicReadCartelPatient,
                       ClinicUpdateCartel)
from v1.models import Cartel as CartelModel
from v1.models import Clinic as ClinicModel
from v1.models import Image as ImageModel
from v1.models import Patient as PatientModel


@dataclass
class CartelService:
    db: Session

    @property
    def query(self) -> Query:
        return self.db.query(CartelModel)

    @property
    def query_w_image(self) -> Query:
        return self.db.query(CartelModel).join(PatientModel).join(ImageModel)

    @property
    def clinic_query(self) -> Query:
        return self.db.query(ClinicModel)


class ClinicCartelService(CartelService):

    def __convert_read(self, cartel: CartelModel) -> ClinicReadCartel:
        patient_model = cartel.patient
        patient = ClinicReadCartelPatient(
            id=str(patient_model.id),
            first_name=patient_model.first_name,
            last_name=patient_model.last_name,
        )
        return ClinicReadCartel(
            id=cartel.id,
            date=cartel.date,
            symptom=cartel.symptom,
            paint_point=cartel.paint_point,
            tempreture=cartel.tempreture,
            pain_start=cartel.pain_start,
            pain_end=cartel.pain_end,
            prior_prescription=cartel.prior_prescription,
            allergy=cartel.allergy,
            prior_issues=cartel.prior_issues,
            patient=patient,
            patient_id=cartel.patient_id,
            doctor_id=cartel.doctor_id,
            diagnosis=cartel.diagnosis,
            prescription=cartel.prescription,
        )

    def list(self, clinic_id: UUID) -> list[ClinicReadCartel]:

        cartel_list = self.query.filter_by(clinic_id=clinic_id).all()

        res = []
        for cartel in cartel_list:
            res.append(self.__convert_read(cartel))
        return res

    def get(self, clinic_id: UUID, id_: UUID) -> ClinicReadCartel:
        cartel = self.query.filter_by(clinic_id=str(clinic_id), id=str(id_)).first()
        if not cartel:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Cartel Not Found")

        res = self.__convert_read(cartel)
        res.images = [i.s3_url for i in cartel.images]
        return res

    def update(self, clinic_id: UUID, id_: UUID, update_cartel: ClinicUpdateCartel):
        cartel = self.query.filter_by(clinic_id=str(clinic_id), id=str(id_)).first()
        if not cartel:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Cartel Not Found")

        cartel.doctor_id = update_cartel.doctor_id
        cartel.diagnosis = update_cartel.diagnosis
        cartel.prescription = update_cartel.prescription
        self.db.flush()
        self.db.refresh(cartel)
