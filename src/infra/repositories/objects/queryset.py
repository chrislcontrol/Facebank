from abc import ABC
from typing import List

from src.domain.types.entity import Entity


class QuerySet(ABC, List):
    def first(self) -> Entity:
        raise NotImplementedError()

    def count(self) -> int:
        raise NotImplementedError()
