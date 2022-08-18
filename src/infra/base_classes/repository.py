from abc import ABC
from typing import List, Optional

from src.domain.types.entity import Entity
from src.infra.base_classes.join_object import JoinQueryset
from src.infra.base_classes.queryset import QuerySet
from src.infra.database.db_connection_handler import DBConnectionHandler
from src.infra.database.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler


class Repository(ABC):
    def __init__(self, model: Entity, db_connection_handler: DBConnectionHandler = None):
        self._db_connection_handler = db_connection_handler or SQLAlchemyConnectionHandler(model=model)

    def _create(self, **fields) -> Entity:
        with self._db_connection_handler as db_handler:
            return db_handler.create(**fields)

    def _get(self, **fields) -> Entity:
        with self._db_connection_handler as db_handler:
            return db_handler.get(**fields)

    def _get_join(self, *, parents_to_join: List[str] = [], **fields) -> JoinQueryset:
        with self._db_connection_handler as db_handler:
            main_obj = db_handler.get(**fields)
            parents = {parent: getattr(main_obj, parent, None) for parent in parents_to_join}
            return JoinQueryset(main=main_obj, **parents)

    def _filter(self, **fields) -> QuerySet[Entity]:
        with self._db_connection_handler as db_handler:
            return db_handler.filter(**fields)
