from sqlalchemy import Column, String

from src.application.extensions import db
from src.infra.database.database_model import DatabaseModel


class ClientDB(db.Model, DatabaseModel):
    __tablename__ = "CLIENT"

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True)
