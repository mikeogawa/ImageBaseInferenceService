import uuid

import sqlalchemy as sa
from settings.db import Base
from sqlalchemy.dialects.postgresql import UUID


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    deleted_at = sa.Column(sa.Boolean, default=None, nullable=True)
