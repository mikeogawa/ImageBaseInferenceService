import sqlalchemy as sq
from common.base_model import Base


class Patient(Base):
    __tablename__ = "user"
    sub_id = sq.Column(sq.String, default="")
    first_name = sq.Column(sq.String, dfault="")
    last_name = sq.Column(sq.String, dfault="")
