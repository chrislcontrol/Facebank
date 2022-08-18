from src.domain.entities.client import Client
from src.domain.entities.user import User
from src.domain.exceptions.user_already_exists import UserAlreadyExists
from src.domain.repositories.user_repository import UserRepository
from src.domain.types.entity import Entity
from src.infra.base_classes.repository import Repository
from src.infra.database.sql_alchemy.models.user import UserDB


class PostgresUserRepository(UserRepository, Repository):
    def __init__(self, model: Entity = UserDB):
        super().__init__(model=model)

    def create_user(self, *, name: str, username: str, password: bytes, client: Client, attributes: dict) -> User:
        return self._create(name=name, username=username, password=password, client=client, attributes=attributes)

    def already_exists(self, *, username: str, client: Client, raise_exception: bool) -> bool:
        obj = self._get(username=username, client=client)
        if obj and raise_exception:
            raise UserAlreadyExists()

        return bool(obj)
