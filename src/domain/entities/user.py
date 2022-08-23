from abc import ABC

from src.domain.entities.client import Client
from src.domain.types.entity import Entity


class User(ABC, Entity):
    name: str
    username: str
    client: Client
    password: str
    attributes: dict
