import sqlalchemy as sq
from common.base_model import BaseModel


class Patient(BaseModel):
    __tablename__ = "user"
    sub_id = sq.Column(sq.String, default="")
    first_name = sq.Column(sq.String, dfault="")
    last_name = sq.Column(sq.String, dfault="")
