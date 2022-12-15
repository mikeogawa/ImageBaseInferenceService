from uuid import UUID

import sqlalchemy as sq
from common.base_model import BaseModel


class Doctor(BaseModel):
    __tablename__ = "doctor"
    clinic_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("clinic.id"), nullable=True),
    sub_id = sq.Column(sq.String, default="")
