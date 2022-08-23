from abc import ABC

from src.domain.entities.client import Client
from src.domain.types.entity import Entity


class Token(ABC, Entity):
    token: str
    client_id: str
    client: Client
