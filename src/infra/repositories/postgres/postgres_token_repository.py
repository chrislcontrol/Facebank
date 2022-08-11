import binascii
import os

from src.domain.repositories.token_repository import TokenRepository
from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.infra.repositories.object_values.repository import Repository
from src.infra.repositories.models.token import TokenDB


class PostgresTokenRepository(TokenRepository, Repository):
    entity = Token

    def create(self, *, client: Client) -> Token:
        token = binascii.hexlify(os.urandom(20)).decode()
        return TokenDB.create(client=client, token=token)

    def get_or_create(self, *, client: Client) -> Token:
        obj = self.convert(TokenDB.query.filter_by(client_id=str(client.id)).first())
        if obj:
            return obj

        return self.create(client=client)
