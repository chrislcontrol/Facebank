from typing import Tuple, Optional

from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.domain.repositories.token_repository import TokenRepository
from src.infra.repositories.sql_alchemy.models.token import TokenDB
from src.infra.repositories.sql_alchemy.helpers.sql_alchemy_repository import SQLAlchemyRepository


class PostgresTokenRepository(TokenRepository, SQLAlchemyRepository):
    db_model = TokenDB

    def create(self, *, client: Client) -> Token:
        model_object = self.db_model(client=client)

        return super().create(obj=model_object)

    def get_or_create(self, *, client: Client) -> Tuple[bool, Token]:
        token = self.get_token(client=client)
        created = not bool(token)

        return created, token or self.create(client=client)

    def get_token(self, *, client: Client) -> Token:
        return self.get(client_id=str(client.id))

    def get_token_by_string_with_client(self, *, token: str) -> Optional[Token]:
        return self.get(token=token)
