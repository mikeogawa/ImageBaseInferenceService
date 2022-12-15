import datetime
import os
from dataclasses import dataclass, field
from typing import Type

from settings.const import DUMMYDATA, S3
from settings.db import Base, SessionContext
from sqlalchemy.orm import Session
from v1.models import Cartel, Clinic, Doctor, Image, Patient

tz = datetime.timezone(datetime.timedelta(hours=9))


@dataclass
class Dummy:
    model: Type[Base]
    index_key: str
    db: Session = field(init=False)

    def set_db(self, db: Session):
        self.db = db

    @property
    def query(self):
        return self.db.query(self.model)

    def create(self, model: Base):
        v = getattr(model, self.index_key)  # force

        exist_model = self.query.get(v)
        if exist_model:
            return exist_model
        self.db.add(model)
        self.db.flush()
        self.db.refresh(model)
        return model


def create():
    with SessionContext() as db:
        clinic_dummy = Dummy(Clinic, "id")
        doctor_dummy = Dummy(Doctor, "id")
        patient_dummy = Dummy(Patient, "id")
        cartel_dummy = Dummy(Cartel, "id")
        image_dummy = Dummy(Image, "id")

        clinic_dummy.set_db(db)
        doctor_dummy.set_db(db)
        patient_dummy.set_db(db)
        cartel_dummy.set_db(db)
        image_dummy.set_db(db)

        clinic1 = clinic_dummy.create(Clinic(
            id="b436e9fb-5277-4882-8757-6272e5749dc7",
            name="MY CLINIC",
        ))
        clinic2 = clinic_dummy.create(Clinic(
            id="65fcfd8b-9000-4eb5-9c9b-38b19d6c5c41",
            name="OTHER CLINIC",
        ))
        print("[CREATE] Clinic", clinic1.id, clinic2.id)

        doctor1 = doctor_dummy.create(Doctor(
            id="e8fa2666-f483-4b17-b054-94e4192143fe",
            clinic_id=clinic1.id,
            sub_id=DUMMYDATA.DOCTOR_SUB_ID,
        ))
        doctor2 = doctor_dummy.create(Doctor(
            id="04d77e2c-2d37-4564-b854-e206d3022649",
            clinic_id=clinic1.id,
            sub_id="other",
        ))
        doctor3 = doctor_dummy.create(Doctor(
            id="1bd7c3df-2a5f-47ca-a3ce-df7030265fa4",
            clinic_id=clinic2.id,
            sub_id="other_clinic",
        ))
        print("[CREATE] Doctor", doctor1.id, doctor2.id, doctor3.id)

        patient1 = patient_dummy.create(Patient(
            id="0fff0c08-b0f7-4d81-a230-5ee044f6a1a2",
            sub_id=DUMMYDATA.PATIENT_SUB_ID,
        ))
        print("[CREATE] Patient", patient1.id)

        cartel1 = cartel_dummy.create(Cartel(
            id="e3d52370-4dd2-49e4-8e59-7fdf6288e6f3",
            clinic_id=clinic1.id,
            doctor_id=doctor1.id,
            date=datetime.datetime(2022, 10, 1, tzinfo=tz),
            symptom="頭痛",
            paint_point="頭",
            tempreture=37.1,
            patient_id=patient1.id,
        ))
        cartel2 = cartel_dummy.create(Cartel(
            id="38670d25-665a-4152-9cba-ca21af3a47bb",
            clinic_id=clinic1.id,
            doctor_id=doctor1.id,
            date=datetime.datetime(2022, 3, 1, tzinfo=tz),
            symptom="足が痛い",
            paint_point="足",
            tempreture=36.1,
            patient_id=patient1.id,
        ))
        print("[CREATE] Cartel", cartel1.id, cartel2.id)

        image1 = image_dummy.create(Image(
            id="a57f6b23-e923-4b50-9b7d-74711e94b3a3",
            cartel_id=cartel1.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "patient", "a57f6b23-e923-4b50-9b7d-74711e94b3a3.png")
        ))

        image2 = image_dummy.create(Image(
            id="ede802af-0e17-4224-ba2c-6ed48886ac70",
            cartel_id=cartel1.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "ede802af-0e17-4224-ba2c-6ed48886ac70.png")
        ))

        image3 = image_dummy.create(Image(
            id="0f182304-26da-463c-a1ec-5884c8a567ab",
            cartel_id=cartel1.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "0f182304-26da-463c-a1ec-5884c8a567ab.png")
        ))

        image4 = image_dummy.create(Image(
            id="d781f12d-244f-45c1-b1ff-8b17ec1c944f",
            cartel_id=cartel2.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "d781f12d-244f-45c1-b1ff-8b17ec1c944f.png")
        ))

        print("[CREATE] Image", image1.id, image2.id, image3.id, image4.id)
        db.commit()


if __name__ == "__main__":
    create()
