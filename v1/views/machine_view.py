from typing import UUID, Optional

from fastapi import APIRouter, Depends, File, Form, UploadFile

from settings.db import SessionDB
from v1.common import IsMachine, StatusOk, machine_auth
from v1.repositories import LocalAnalyzeRepository, LocalPatientRepository
from v1.schemas import MachineWrite
from v1.use_cases import machine as use_case_machine

router = APIRouter()


@router.post("/upload_image/", response_model=StatusOk)
def upload_image(
    cartel_id: UUID = Form(...),
    user_id: UUID = Form(...),
    file: bytes = File(...),
    patient_repository: LocalPatientRepository = Depends(),
    machine: Optional[IsMachine] = Depends(machine_auth),
):
    payload = {"cartel_id": cartel_id, "user_id": user_id}

    with SessionDB() as db:
        use_case = use_case_machine.RegiserImage(db, patient_repository)
        use_case.execute(payload, file)

    return StatusOk()


@router.post("/update_score/", response_model=StatusOk)
def update_score(
    payload: MachineWrite,
    file: UploadFile = File(),
    analyze_repository: LocalAnalyzeRepository = Depends(),
    machine: Optional[IsMachine] = Depends(machine_auth),
):

    with SessionDB() as db:
        use_case = use_case_machine.UpdateScore(db, analyze_repository)
        use_case.execute(payload.dict())

    return StatusOk
