from dataclasses import dataclass

from src.domain.types.entity import Entity


@dataclass
class Token(Entity):
    token: str
    client_id: str
