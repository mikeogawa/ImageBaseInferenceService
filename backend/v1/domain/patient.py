from dataclasses import dataclass
from uuid import UUID


@dataclass
class Patient:

    id: UUID
    first_name: str
    last_name: str
