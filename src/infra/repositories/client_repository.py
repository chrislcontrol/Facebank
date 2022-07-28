from src.infra.entities.client import Client


class ClientRepository:
    def create_client(self, *, username: str, password: str) -> Client:
        return Client.create(username=username, password=password)
