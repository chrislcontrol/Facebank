from __future__ import annotations

import uuid
from datetime import date, datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.infra.database.database_model import DatabaseModel


class SQLAlchemyDatabaseModel(DatabaseModel):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        new_dict = {}
        for key, value in vars(self).copy().items():
            if not key.startswith('_') and not isinstance(value, DatabaseModel):
                if isinstance(value, (date, datetime)):
                    value = value.isoformat()

                elif isinstance(value, bytes):
                    value = value.decode('utf-8')

                new_dict[key] = value

        return new_dict
