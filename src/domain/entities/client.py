from dataclasses import dataclass

from src.domain.types.entity import Entity


@dataclass
class Client(Entity):
    username: str
    email: str
    password: str
