import sqlalchemy as sq
from common.base_model import Base


class Clinic(Base):
    __tablename__ = "clinic"
    name = sq.Column(sq.String, default="")
