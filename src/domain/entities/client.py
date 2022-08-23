from abc import ABC

from src.domain.types.entity import Entity


class Client(ABC, Entity):
    username: str
    email: str
    password: str
