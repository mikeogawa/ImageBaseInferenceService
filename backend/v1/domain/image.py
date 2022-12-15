from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from v1.repositories import BaseAnalyzeRepostiory, BasePatientRepository


@dataclass
class ClinicImage:
    id: UUID
    s3_url: str
    score: float
    cartel_id: UUID
    user_id: UUID
    analyze_repoitory: BaseAnalyzeRepostiory

    def reanalyze(self):
        self.analyze_repoitory.run(self.user_id, self.id)


@dataclass
class MachineImage:
    score: float
    cartel_id: UUID
    user_id: UUID
    patient_repository: Optional[BasePatientRepository] = None
    analyze_repoitory: Optional[BaseAnalyzeRepostiory] = None
    s3_url: str = ""
    id: Optional[UUID] = None

    def update_image(self, image: bytes):
        self.patient_repository.post_image(image, self.user_id, self.id)
