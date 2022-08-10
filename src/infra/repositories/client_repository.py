from src.data.interfaces.client_repository_interface import IClientRepository
from src.domain.entities.client import Client
from src.infra.models.client import ClientDB


class ClientRepository(IClientRepository):
    entity = Client

    def create_client(self, *, username: str, password: str, email: str) -> Client:
        client_db = ClientDB.create(username=username, password=password, email=email)
        return client_db

    def get_by_username(self, username: str) -> Client:
        query = ClientDB.query.filter_by(username=username).first()
        return self.convert(query)
