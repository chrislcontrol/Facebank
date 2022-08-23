from abc import ABC, abstractmethod
from datetime import datetime


class Entity:
    id: str
    created: datetime
    modified: datetime

    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()
