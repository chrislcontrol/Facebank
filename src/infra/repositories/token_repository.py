import binascii
import os

from src.data.interfaces.token_repository_interface import ITokenRepository
from src.domain.entities.client import Client
from src.domain.entities.token import Token
from src.infra.models.client import ClientDB
from src.infra.models.token import TokenDB


class TokenRepository(ITokenRepository):
    entity = Token

    def create(self, *, client: Client) -> Token:
        token = binascii.hexlify(os.urandom(20)).decode()
        return TokenDB.create(client=client, token=token)

    def get_or_create(self, *, client: Client) -> Token:
        obj = self.convert(TokenDB.query.filter_by(client_id=str(client.id)).first())
        if obj:
            return obj

        return self.create(client=client)
