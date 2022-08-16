from abc import ABC
from datetime import datetime, date


class Entity(ABC):
    id: str
    created: datetime
    modified: datetime

    def to_dict(self) -> dict:
        raise NotImplementedError
