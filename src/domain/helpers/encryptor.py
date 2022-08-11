from abc import abstractmethod, ABC
from typing import Union
from uuid import UUID


class IEncryptor(ABC):
    @abstractmethod
    def encrypt(self, value: Union[str, UUID], hashed: bytes = None) -> bytes:
        raise NotImplementedError()
