import binascii
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from src.infra.database.sql_alchemy.config import Base
from src.infra.database.sql_alchemy.sql_alchemy_database_model import SQLAlchemyDatabaseModel


class TokenDB(Base, SQLAlchemyDatabaseModel):
    __tablename__ = "TOKEN"

    client_id = Column(UUID(as_uuid=True), ForeignKey('CLIENT.id'))
    client = relationship("ClientDB", foreign_keys=[client_id], backref=backref("token", uselist=False))
    token = Column(String, nullable=False, default=lambda: binascii.hexlify(os.urandom(20)).decode())
