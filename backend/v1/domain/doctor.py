from dataclasses import dataclass
from uuid import UUID


@dataclass
class Doctor:
    id: UUID
    sub_id: UUID
