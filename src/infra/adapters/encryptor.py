from typing import Union
from uuid import UUID

import bcrypt

from src.data.interfaces.encryptor_interface import IEncryptor


class Encryptor(IEncryptor):
    def encrypt(self, value: Union[str, UUID], hashed: bytes = None) -> bytes:
        if not isinstance(value, (bytes, str)):
            raise TypeError(f'Expected {Union[str, bytes]} and received {type(value)}.')

        encoded = value if isinstance(value, bytes) else value.encode()
        return bcrypt.hashpw(encoded, hashed or bcrypt.gensalt())
