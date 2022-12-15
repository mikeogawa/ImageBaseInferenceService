from pydantic import Base


class StatusOk(Base):
    status: str = "200"
    detail: str = "OK"
