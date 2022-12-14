from uuid import UUID

from pydantic import BaseModel


class AnalyzeBase(BaseModel):
    cartel_id: UUID
    image_id: UUID


class AnalyzeWrite(AnalyzeBase):
    pass
