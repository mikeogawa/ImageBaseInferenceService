from dataclasses import dataclass
from typing import Any, Dict, Optional
from uuid import UUID

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Query, Session, joinedload
from starlette.status import HTTP_400_BAD_REQUEST
from v1.domain import Patient
from v1.models import Cartel as CartelModel
from v1.models import Patient as PatientModel


@dataclass
class PatientService:
    db: Session

    @property
    def query(self) -> Query:
        return self.db.query(PatientModel)

    @property
    def cartel_query(self) -> Query:
        return self.db.query(CartelModel).options(joinedload(CartelModel.patient))


@dataclass
class ClinicPatientService(PatientService):
    def validate_cartel(self, clinic_id: UUID, cartel_id: UUID):
        cartel = self.cartel_query.filter_by(id=str(cartel_id), clinic_id=str(clinic_id))
        if not cartel:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Cartel Not Found")

    def get_by_cartel(self, id: UUID) -> Patient:
        cartel = self.cartel_query.filter_by(id=str(id)).first()
        if not cartel:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Image Not Found")

        patient = cartel.patient

        return Patient(
            id=patient.id,
            first_name=patient.first_name,
            last_name=patient.last_name,
        )
