from typing import TypeVar, Generic

from src.domain.types.entity import Entity

_Wrapped = TypeVar('_Wrapped')


class QuerySet(Generic[_Wrapped]):
    def first(self) -> Entity:
        raise NotImplementedError()

    def count(self) -> int:
        raise NotImplementedError()
