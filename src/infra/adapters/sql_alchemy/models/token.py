import binascii
import os

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref

from src.application.extensions import db
from src.infra.adapters.sql_alchemy.sql_alchemy_database_model import SQLAlchemyDatabaseModel


class TokenDB(db.Model, SQLAlchemyDatabaseModel):
    __tablename__ = "TOKEN"

    client_id = db.Column(UUID(as_uuid=True), db.ForeignKey('CLIENT.id'))
    client = db.relationship("ClientDB", foreign_keys=[client_id], backref=backref("token", uselist=False))
    token = db.Column(String, nullable=False, default=lambda: binascii.hexlify(os.urandom(20)).decode())
