from dataclasses import dataclass

from src.domain.helpers.entity import Entity


@dataclass
class Token(Entity):
    token: str
    client_id: str
