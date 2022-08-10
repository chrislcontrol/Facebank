from typing import Union

import bcrypt

from src.data.interfaces.encryptor import IEncryptor


class Encryptor(IEncryptor):
    def encrypt(self, value: Union[str, bytes]) -> bytes:
        if not isinstance(value, (bytes, str)):
            raise TypeError(f'Expected {Union[str, bytes]} and received {type(value)}.')

        encoded = value if isinstance(value, bytes) else value.encode()
        return bcrypt.hashpw(encoded, bcrypt.gensalt())
