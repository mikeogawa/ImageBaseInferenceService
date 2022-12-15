import datetime
import os
from dataclasses import dataclass, field
from typing import Type

from settings.const import DUMMYDATA, S3
from settings.db import Base, SessionDB
from sqlalchemy.orm import Session
from v1.models import Cartel, Clinic, Doctor, Image, Patient

tz = datetime.timezone(datetime.timedelta(housr=9))


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

        if self.query.get(getattr(self.model, self.index_key) == v):
            return
        self.query.add(model)
        self.db.commit()
        self.db.flush()
        return model


def create():
    with SessionDB() as db:
        clinic_dummy = Dummy(Clinic, "id")
        doctor_dummy = Dummy(Doctor, "sub_id")
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
            id="a5b6b95e-eb5f-4727-a237-182e8702be2b",
            clinic_id=clinic1.id,
            sub_id=DUMMYDATA.DOCTOR_SUB_ID,
        ))
        doctor2 = doctor_dummy.create(Doctor(
            id="e3f554c5-3ea3-4778-9f27-09a2cf945c44",
            clinic_id=clinic1.id,
            sub_id="other",
        ))
        doctor3 = doctor_dummy.create(Doctor(
            id="f44ce4e2-0790-44cb-8d3a-da304a6c9b13",
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
            date=datetime.datetime(2022, 10, 1, tzinfo=tz),
            symtom="頭痛",
            paint_point="頭",
            tempreture=37.1,
            patient_id=patient1.id,
        ))
        cartel2 = cartel_dummy.create(Cartel(
            id="38670d25-665a-4152-9cba-ca21af3a47bb",
            clinic_id=clinic1.id,
            date=datetime.datetime(2022, 3, 1, tzinfo=tz),
            symtom="足が痛い",
            paint_point="足",
            tempreture=36.1,
            patient_id=patient1.id,
        ))
        print("[CREATE] Cartel", cartel1.id, cartel2.id)

        image1 = image_dummy.create(Image(
            id="a57f6b23-e923-4b50-9b7d-74711e94b3a3",
            carte_id=cartel1.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "patient", "a57f6b23-e923-4b50-9b7d-74711e94b3a3.png")
        ))

        image2 = image_dummy.create(Image(
            id="ede802af-0e17-4224-ba2c-6ed48886ac70",
            carte_id=cartel1.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "ede802af-0e17-4224-ba2c-6ed48886ac70.png")
        ))

        image3 = image_dummy.create(Image(
            id="0f182304-26da-463c-a1ec-5884c8a567ab",
            carte_id=cartel1.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "0f182304-26da-463c-a1ec-5884c8a567ab.png")
        ))

        image4 = image_dummy.create(Image(
            id="d781f12d-244f-45c1-b1ff-8b17ec1c944f",
            carte_id=cartel2.id,
            s3_url=os.path.join(S3.LOCAL_DIR, S3.S3_BUCKETNAME, "d781f12d-244f-45c1-b1ff-8b17ec1c944f.png")
        ))

        print("[CREATE] Image", image1.id, image2.id, image3.id, image4.id)


if __name__ == "__main__":
    create()
