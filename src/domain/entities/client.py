from dataclasses import dataclass

from src.domain.helpers.entity import Entity


@dataclass
class Client(Entity):
    id: str
    username: str
    email: str
