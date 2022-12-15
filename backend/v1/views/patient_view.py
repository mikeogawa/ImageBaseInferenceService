from typing import Optional

from fastapi import APIRouter, Depends

from settings.db import SessionDB
from v1 import use_cases
from v1.common import StatusOk, patient_auth
from v1.models import Patient as PatientModel
from v1.schemas import QuestionnaireWrite

router = APIRouter()


@router.post("/fill_cartel/", response_model=StatusOk)
def fill_cartel(
    payload: QuestionnaireWrite,
    patient: Optional[PatientModel] = Depends(patient_auth)
):

    with SessionDB() as db:
        use_case = use_cases.patient.FillCartel(db=db)
        use_case.execute(patient, payload.dict())
        db.commit()

    return StatusOk()
