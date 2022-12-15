import datetime

import sqlalchemy as sq
from sqlalchemy.dialects.postgresql import UUID
from v1.common.base_model import BaseModel


class Cartel(BaseModel):
    __tablename__ = "cartel"
    clinic_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("clinic.id"), nullable=True)

    # patient
    date = sq.Column(sq.DateTime, default=datetime.datetime.now)
    symptom = sq.Column(sq.String, default="")
    paint_point = sq.Column(sq.String, default="")
    tempreture = sq.Column(sq.Float, default=0.)
    pain_start = sq.Column(sq.DateTime, nullable=True)
    pain_end = sq.Column(sq.DateTime, nullable=True)
    prior_prescription = sq.Column(sq.String, default="")
    allergy = sq.Column(sq.String, default="")
    prior_issues = sq.Column(sq.String, default="")
    patient_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("patient.id", ondelete="CASCADE"))

    # doctor
    diagnosis = sq.Column(sq.String, default="")
    prescription = sq.Column(sq.String, default="")
    doctor_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("doctor.id"), nullable=True)

    clinic = sq.orm.relationship("Clinic", backref="cartels")
    patient = sq.orm.relationship("Patient", backref="cartels")
    doctor = sq.orm.relationship("Doctor", backref="cartels")
