from __future__ import annotations

import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.infra.config.db_connection_handler import DBConnectionHandler

Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()


class DatabaseModel:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    @classmethod
    def create(cls, **kwargs) -> object:
        new_object = cls(**kwargs)
        return cls.__save_object(new_object)

    def save(self) -> Base:
        return self.__save_object(self)

    @classmethod
    def __save_object(cls, obj: object) -> object:
        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.add(obj)
                db_connection.session.commit()

                return obj
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
