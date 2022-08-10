from sqlalchemy import Column, String

from src.domain.entities.client import Client
from src.infra.config.database import DatabaseModel
from src.main.config.extensions import db


class ClientDB(db.Model, DatabaseModel):
    __tablename__ = "CLIENT"
    __entity__ = Client

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True)
