from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref

from src.application.extensions import db
from src.infra.database.database_model import DatabaseModel


class TokenDB(db.Model, DatabaseModel):
    __tablename__ = "TOKEN"

    client_id = db.Column(UUID, db.ForeignKey('CLIENT.id'))
    client = db.relationship("ClientDB", foreign_keys=[client_id], backref=backref("token", uselist=False))
    token = db.Column(String, nullable=False)
