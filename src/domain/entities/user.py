from src.domain.entities.client import Client
from src.domain.types.entity import Entity


class User(Entity):
    name: str
    username: str
    client: Client
    password: str
    attributes: dict
