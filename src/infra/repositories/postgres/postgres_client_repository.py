from src.domain.entities.client import Client
from src.domain.repositories.client_repository import ClientRepository
from src.infra.adapters.sql_alchemy.models.client import ClientDB
from src.infra.database.db_connection_handler import DBConnectionHandler


class PostgresClientRepository(ClientRepository):
    entity = ClientDB

    def __init__(self, db_connection_handler: DBConnectionHandler):
        self.db_connection_handler = db_connection_handler

    def create_client(self, *, username: str, password: str, email: str) -> Client:
        return self.create(username=username, password=password, email=email)

    def get_by_username(self, username: str) -> Client:
        return self.get(username=username)

    def already_exists(self, username: str) -> bool:
        return bool(self.get_by_username(username=username))
