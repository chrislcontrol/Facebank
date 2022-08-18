from src.domain.entities.client import Client
from src.domain.types.entity import Entity


class Token(Entity):
    token: str
    client_id: str
    client: Client
