from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from fastapi import UploadFile
from v1.repositories import BaseAnalyzeRepostiory, BasePatientRepository


@dataclass
class ClinicImage:
    id: UUID
    s3_url: str
    score: float
    is_analyzing: bool
    cartel_id: str
    analyze_repoitory: BaseAnalyzeRepostiory

    def reanalyze(self):
        self.analyze_repoitory.run(self.cartel_id, self.id)


@dataclass
class MachineImage:
    cartel_id: str
    is_analyzing: bool = True
    score: float = 0.
    s3_url: str = ""
    id: Optional[UUID] = None
    patient_repository: Optional[BasePatientRepository] = None
    analyze_repoitory: Optional[BaseAnalyzeRepostiory] = None

    def update_id(self, id_: UUID):
        self.id = id_

    def update_image(self, image: UploadFile):
        self.patient_repository.post_image(image.file, str(self.cartel_id), str(self.id))
