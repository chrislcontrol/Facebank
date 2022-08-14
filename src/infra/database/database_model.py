from __future__ import annotations

import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func

from src.domain.types.entity import Entity
from src.infra.database.db_connection_handler import DBConnectionHandler
from src.infra.repositories.object_values.model_object import ModelObject
from src.utils.objects import serialize_object


class DatabaseModel:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def get(cls, **kwargs):
        queryset = cls.query.filter_by(**kwargs)  # noqa
        count = queryset.count()
        if count > 1:
            raise IntegrityError(f'Expected 1 result bot got {count}.')

        return queryset.first()

    @classmethod
    def create(cls, **kwargs) -> ModelObject:
        valid_kwargs = {}
        for key, value in kwargs.items():
            if isinstance(value, (ModelObject, Entity)):
                valid_kwargs[f"{key}_id"] = str(value.id)
            else:
                valid_kwargs[key] = value

        new_object = cls(**valid_kwargs)
        return cls.__save_object(new_object)

    def __str__(self):
        return f"< {self.__class__.__name__}[{self.id}] >"

    @classmethod
    def __save_object(cls, obj: object) -> ModelObject:
        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.add(obj)
                db_connection.session.commit()
                obj.id  # noqa

                return ModelObject(**serialize_object(obj))
            except Exception:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def __repr__(self):
        pk = getattr(self, "id", None)
        pk_repr = f"[id={pk}]" if pk else ""

        return f"{self.__class__.__qualname__}{pk_repr}"

    def __eq__(self, other) -> bool:
        all_attr = vars(self)
        for key, value in all_attr.items():
            if not hasattr(other, key):
                return False

            if value != getattr(other, key):
                return False

        return True
