from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends
from settings.db import SessionContext
from v1.auth import clinic_auth
from v1.common import StatusOk
from v1.models import Doctor as DoctorModel
from v1.repositories import BaseAnalyzeRepostiory, LocalAnalyzeRepository
from v1.schemas import (AnalyzeWrite, CartelRead, CartelWrite, ImageRead,
                        PatientRead)
from v1.use_cases import clinic as use_case_clinic

router = APIRouter(tags=['Clinic'])


@router.get("/cartels/", response_model=list[CartelRead])
def list_cartels(
    doctor: Optional[DoctorModel] = Depends(clinic_auth),
):

    with SessionContext() as db:
        use_case = use_case_clinic.ListCartel(db=db)
        res = use_case.execute(doctor)
    return res


@router.get("/cartels/{cartel_id}/", response_model=CartelRead)
def get_cartel(
    cartel_id: UUID,
    doctor: Optional[DoctorModel] = Depends(clinic_auth),
):

    with SessionContext() as db:
        use_case = use_case_clinic.GetCartel(db=db)
        obj = use_case.execute(doctor, cartel_id)

    return obj


@router.get("/cartels/{cartel_id}/images/", response_model=list[ImageRead])
def get_cartel_images(
    cartel_id: UUID,
    doctor: Optional[DoctorModel] = Depends(clinic_auth),
):

    with SessionContext() as db:
        use_case = use_case_clinic.ListCartelImage(db=db)
        obj = use_case.execute(doctor, cartel_id)

    return obj


@router.get("/cartels/{cartel_id}/patient/", response_model=PatientRead)
def get_cartel_patient(
    cartel_id: UUID,
    doctor: Optional[DoctorModel] = Depends(clinic_auth),
):

    with SessionContext() as db:
        use_case = use_case_clinic.GetCartelPatient(db=db)
        obj = use_case.execute(doctor, cartel_id)

    return obj


@router.get("/cartels/{cartel_id}/images/{image_id}/", response_model=ImageRead)
def get_image(
    cartel_id: UUID,
    image_id: UUID,
    doctor: Optional[DoctorModel] = Depends(clinic_auth),

):

    with SessionContext() as db:
        use_case = use_case_clinic.GetCartelImage(db)
        obj = use_case.execute(doctor, cartel_id, image_id)

    return obj


@router.put("/cartels/{cartel_id}/", response_model=StatusOk)
def update_cartel(
    cartel_id: UUID,
    payload: CartelWrite,
    doctor: Optional[DoctorModel] = Depends(clinic_auth),
):
    with SessionContext() as db:
        use_case = use_case_clinic.UpdateCartel(db=db)
        use_case.execute(doctor, cartel_id, payload.dict())

    return StatusOk()


@router.post("/re_anaylze_image/", response_model=StatusOk)
def analyze(
    payload: AnalyzeWrite,
    analyze_repository: BaseAnalyzeRepostiory = Depends(lambda: LocalAnalyzeRepository()),
    doctor: Optional[DoctorModel] = Depends(clinic_auth),
):

    with SessionContext() as db:
        use_case = use_case_clinic.ReAnalyze(db, analyze_repository)
        use_case.execute(doctor, payload.dict())

    return StatusOk()
