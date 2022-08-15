from __future__ import annotations

import uuid

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
