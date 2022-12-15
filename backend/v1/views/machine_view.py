from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, UploadFile
from settings.db import SessionContext
from v1.auth import IsMachine, machine_auth
from v1.common import StatusOk
from v1.repositories import (BaseAnalyzeRepostiory, BasePatientRepository,
                             LocalAnalyzeRepository, LocalPatientRepository)
from v1.schemas import MachineWrite
from v1.use_cases import machine as use_case_machine

router = APIRouter(tags=['Machine'])


@router.post("/upload_image/", response_model=StatusOk)
def upload_image(
    cartel_id: UUID = Form(...),
    file: UploadFile = File(...),
    patient_repository: BasePatientRepository = Depends(lambda: LocalPatientRepository()),
    machine: Optional[IsMachine] = Depends(machine_auth),  # noqa
):
    payload = {"cartel_id": cartel_id}

    with SessionContext() as db:
        use_case = use_case_machine.RegiserImage(db, patient_repository)
        use_case.execute(payload, file)

    return StatusOk()


@router.post("/update_score/", response_model=StatusOk)
def update_score(
    payload: MachineWrite,
    analyze_repository: BaseAnalyzeRepostiory = Depends(lambda: LocalAnalyzeRepository()),
    machine: Optional[IsMachine] = Depends(machine_auth),
):

    with SessionContext() as db:
        use_case = use_case_machine.UpdateScore(db, analyze_repository)
        use_case.execute(payload.dict())

    return StatusOk()
