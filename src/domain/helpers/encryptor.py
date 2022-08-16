from abc import abstractmethod, ABC
from typing import Union
from uuid import UUID


class Encryptor(ABC):
    @abstractmethod
    def encrypt(self, value: Union[str, UUID], hashed: bytes = None) -> bytes:
        raise NotImplementedError()

    @abstractmethod
    def encrypt_password(self, value: Union[str, UUID]) -> bytes:
        raise NotImplementedError()
