import datetime

import sqlalchemy as sq
from common.base_model import Base
from sqlalchemy.dialects.postgresql import UUID


class Cartel(Base):
    __tablename__ = "cartel"
    clinic_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("clinic.id"), nullable=True)

    # patient
    date = sq.Column(sq.DateTime, default=datetime.datetime.now)
    summary = sq.Column(sq.String, default="")
    symptom = sq.Column(sq.String, default="")
    paint_point = sq.Column(sq.String, default="")
    tempreture = sq.Column(sq.Float, default=0.)
    pain_start = sq.Column(sq.DateTime)
    pain_end = sq.Column(sq.DateTime)
    prior_prescription = sq.Column(sq.String, default="")
    allergy = sq.Column(sq.String, default="")
    prior_issues = sq.Column(sq.String, default="")
    patient_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("patient.id", ondelete="CASCADE"))

    # doctor
    doctor_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("doctor.id"), nullable=True)
    diagnosis = sq.Column(sq.String, default="")
    prescription = sq.Column(sq.String, default="")

    patient = sq.orm.relationship("patient", backref="cartel")
