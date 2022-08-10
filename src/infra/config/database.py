from __future__ import annotations

import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import func

from src.domain.helpers.entity import Entity
from src.infra.config.db_connection_handler import DBConnectionHandler
from src.infra.helpers.model_object import ModelObject

Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()


class DatabaseModel:
    __entity__ = ModelObject

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def create(cls, **kwargs) -> __entity__:
        valid_kwargs = {}
        for key, value in kwargs.items():
            if isinstance(value, (ModelObject, Entity)):
                valid_kwargs[f"{key}_id"] = str(value.id)
            else:
                valid_kwargs[key] = value

        new_object = cls(**valid_kwargs)
        return cls.__save_object(new_object)

    @classmethod
    def __save_object(cls, obj: object) -> __entity__:
        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.add(obj)
                model_object = cls.__entity__(
                    id=None,
                    created=None,
                    modified=None,
                    **{key: value for key, value in vars(obj).items() if not key.startswith('_')}
                )
                db_connection.session.commit()
                model_object.id = obj.id
                model_object.created = obj.created
                model_object.modified = obj.modified

                return model_object
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
