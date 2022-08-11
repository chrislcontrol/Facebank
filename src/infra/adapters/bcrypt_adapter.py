from typing import Union
from uuid import UUID

import bcrypt

from src.domain.helpers.encryptor import IEncryptor


class BcryptAdapter(IEncryptor):
    def encrypt(self, value: Union[str, UUID], hashed: bytes = None) -> bytes:
        if not isinstance(value, (bytes, str)):
            raise TypeError(f'Expected {Union[str, bytes]} and received {type(value)}.')

        encoded = value if isinstance(value, bytes) else value.encode()
        return bcrypt.hashpw(encoded, hashed or bcrypt.gensalt())
