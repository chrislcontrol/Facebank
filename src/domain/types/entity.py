from abc import ABC
from dataclasses import dataclass
from datetime import datetime


class Entity(ABC):
    id: str
    created: datetime
    modified: datetime

    def to_dict(self) -> dict:
        raise NotImplementedError
