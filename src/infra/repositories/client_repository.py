from typing import Optional

from src.data.interfaces.client_repository_interface import IClientRepository
from src.domain.entities.client import Client
from src.infra.models.client import ClientDB


class ClientRepository(IClientRepository):
    def create_client(self, *, username: str, password: str, email: str) -> Client:
        client_db = ClientDB.create(username=username, password=password, email=email)
        return self.__convert(client_db)

    def get_by_username(self, username: str) -> Client:
        query = ClientDB.query.filter_by(username=username).first()
        return self.__convert(query)

    def __convert(self, obj) -> Optional[Client]:
        def convert(db_obj):
            return Client(id=db_obj.id, username=db_obj.username, email=db_obj.email)

        if not obj:
            return None

        if isinstance(obj, list):
            for item in obj:
                return convert(item)

        return convert(obj)
