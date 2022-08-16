from abc import abstractmethod, ABC
from enum import Enum


class BaseFieldProtocol(ABC):
    @abstractmethod
    def validate(self, value: any) -> (bool, Enum):
        raise NotImplementedError()
