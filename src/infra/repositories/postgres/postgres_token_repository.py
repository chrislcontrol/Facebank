from typing import Tuple, Optional

from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.domain.repositories.token_repository import TokenRepository
from src.infra.adapters.sql_alchemy.models.token import TokenDB
from src.infra.database.db_connection_handler import DBConnectionHandler


class PostgresTokenRepository(TokenRepository):
    entity = TokenDB

    def __init__(self, db_connection_handler: DBConnectionHandler):
        self.db_connection_handler = db_connection_handler

    def get_or_create(self, *, client: Client) -> Tuple[bool, Token]:
        token = self.get_token(client=client)
        created = not bool(token)

        return created, token or self.create(client=client)

    def get_token(self, *, client: Client) -> Token:
        return self.get(client_id=str(client.id))

    def get_token_by_string_with_client(self, *, token: str) -> Optional[Token]:
        return self.get(token=token)
