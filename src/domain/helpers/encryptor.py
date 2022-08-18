from abc import abstractmethod, ABC
from typing import Union
from uuid import UUID


class Encryptor(ABC):
    @abstractmethod
    def encrypt_password(self, value: Union[str, UUID], salt: bytes = None) -> bytes:
        raise NotImplementedError()
