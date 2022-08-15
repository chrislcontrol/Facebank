from src.domain.types.entity import Entity


class Client(Entity):
    username: str
    email: str
    password: str
