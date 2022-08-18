from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import backref, relationship

from src.infra.database.sql_alchemy.config import Base
from src.infra.database.sql_alchemy.sql_alchemy_database_model import SQLAlchemyDatabaseModel


class UserDB(Base, SQLAlchemyDatabaseModel):
    __tablename__ = "USER"

    client_id = Column("CLIENT_ID", UUID(as_uuid=True), ForeignKey('CLIENT.id'))
    client = relationship("ClientDB", foreign_keys=[client_id], backref=backref("users", uselist=False))
    name = Column("NAME", String(100), nullable=False)
    username = Column("USERNAME", String(100))
    password = Column(String, nullable=False)
    attributes = Column(JSONB, default={})

    __table_args__ = (UniqueConstraint('CLIENT_ID', 'USERNAME', name='_client_username_uc'),)
