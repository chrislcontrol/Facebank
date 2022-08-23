from abc import ABC
from typing import Type

from src.domain.types.entity import Entity
from src.infra.base_classes.queryset import QuerySet
from src.infra.database.db_connection_handler import DBHandler


class Repository(ABC):
    entity: Type[Entity] = None

    def __init__(self, db: DBHandler):
        self._db = db

    def _create(self, **fields):
        entity = self.entity(**fields)
        return self._db.create(entity)

    def _get(self, **fields):
        return self._db.get(entity=self.entity, **fields)

    def _filter(self, **fields) -> QuerySet:
        return self._db.filter(entity=self.entity, **fields)
