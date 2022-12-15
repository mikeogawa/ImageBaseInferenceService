from fastapi import APIRouter
from v1.views import clinic_view, machine_view, patient_view

router = APIRouter()

router.include_router(patient_view.router)
router.include_router(clinic_view.router)
router.include_router(machine_view.router)
