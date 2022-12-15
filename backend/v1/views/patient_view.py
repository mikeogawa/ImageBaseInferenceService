from typing import Optional

from fastapi import APIRouter, Depends
from settings.db import SessionContext
from v1.auth import patient_auth
from v1.common import StatusOk
from v1.models import Patient as PatientModel
from v1.schemas import QuestionnaireWrite
from v1.use_cases import patient as use_case_patient

router = APIRouter(tags=['Patient'])


@router.post("/fill_cartel/", response_model=StatusOk)
def fill_cartel(
    payload: QuestionnaireWrite,
    patient: Optional[PatientModel] = Depends(patient_auth)
):

    with SessionContext() as db:
        use_case = use_case_patient.FillQuestionnare(db=db)
        use_case.execute(patient, payload.dict())
        db.commit()

    return StatusOk()
