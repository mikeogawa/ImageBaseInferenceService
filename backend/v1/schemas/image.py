from uuid import UUID

from pydantic import BaseModel


class ImageBase(BaseModel):
    s3_url: str
    score: float
    is_analyzing: bool


class ImageRead(ImageBase):
    id: UUID


class ImageWrite(ImageBase):
    pass
