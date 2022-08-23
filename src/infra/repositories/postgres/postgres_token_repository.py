from typing import Tuple

from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.domain.repositories.token_repository import TokenRepository
from src.infra.base_classes.repository import Repository
from src.infra.database.sql_alchemy.models.token import TokenDB


class PostgresTokenRepository(TokenRepository, Repository):
    entity = TokenDB

    def get_or_create(self, *, client: Client) -> Tuple[bool, Token]:
        token = self.get_token(client=client)
        created = not bool(token)

        return created, token or self._create(client=client)

    def get_token(self, *, client: Client) -> Token:
        return self._get(client_id=str(client.id))

    def get_token_by_string(self, *, token: str) -> Token:
        return self._get(token=token)
