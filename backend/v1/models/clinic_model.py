import sqlalchemy as sq
from common.base_model import BaseModel


class Clinic(BaseModel):
    __tablename__ = "clinic"
    name = sq.Column(sq.String, default="")
