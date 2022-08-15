from sqlalchemy import Column, String

from src.application.extensions import db
from src.infra.adapters.sql_alchemy.sql_alchemy_database_model import SQLAlchemyDatabaseModel


class ClientDB(db.Model, SQLAlchemyDatabaseModel):
    __tablename__ = "CLIENT"

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True)
