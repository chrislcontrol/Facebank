from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref

from src.domain.entities.token import Token
from src.infra.config.database import DatabaseModel
from src.application.extensions import db


class TokenDB(db.Model, DatabaseModel):
    __tablename__ = "TOKEN"
    __entity__ = Token

    client_id = db.Column(UUID, db.ForeignKey('CLIENT.id'))
    client = db.relationship("ClientDB", foreign_keys=[client_id], backref=backref("token", uselist=False))
    token = db.Column(String, nullable=False)
