import sqlalchemy as sq
from sqlalchemy.dialects.postgresql import UUID
from v1.common.base_model import BaseModel


class Image(BaseModel):
    __tablename__ = "image"
    s3_url = sq.Column(sq.String, default="")
    score = sq.Column(sq.Float, default=0.)
    is_analyzing = sq.Column(sq.Boolean, default=True)
    cartel_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey("cartel.id", ondelete="CASCADE"))
    cartel = sq.orm.relationship("Cartel", backref="images")
