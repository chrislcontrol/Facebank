import binascii
import os
from typing import Tuple, Optional

from src.domain.repositories.token_repository import TokenRepository
from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.infra.repositories.object_values.repository import Repository
from src.infra.repositories.models.token import TokenDB


class PostgresTokenRepository(TokenRepository, Repository):
    entity = Token
    model = TokenDB

    def create(self, *, client: Client) -> Token:
        token = binascii.hexlify(os.urandom(20)).decode()
        model_object = self.model.create(client=client, token=token)
        return self.convert(model_object)

    def get_or_create(self, *, client: Client) -> Tuple[bool, Token]:
        token = self.get_token(client=client)
        created = not bool(token)

        return created, token or self.create(client=client)

    def get_token(self, *, client: Client) -> Token:
        queryset = self.model.query.filter_by(client_id=str(client.id))
        obj = self.convert(queryset.first())
        if obj:
            return obj

    def get_token_by_string_with_client(self, *, token: str) -> Tuple[Optional[Token], Optional[Client]]:
        queryset = self.model.get(token=token)
        if not queryset:
            return None, None

        token = self.convert(queryset)
        client = self.convert(queryset.client, entity=Client)
        return token, client

