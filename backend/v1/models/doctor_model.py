import sqlalchemy as sq
from sqlalchemy.dialects.postgresql import UUID
from v1.common.base_model import BaseModel


class Doctor(BaseModel):
    __tablename__ = "doctor"
    clinic_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("clinic.id"), nullable=True)
    sub_id = sq.Column(sq.String, default="")

    clinic = sq.orm.relationship("Clinic", backref="doctors")
