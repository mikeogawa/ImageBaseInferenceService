import sqlalchemy as sq
from v1.common.base_model import BaseModel


class Patient(BaseModel):
    __tablename__ = "patient"
    sub_id = sq.Column(sq.String, default="")
    first_name = sq.Column(sq.String, default="")
    last_name = sq.Column(sq.String, default="")
