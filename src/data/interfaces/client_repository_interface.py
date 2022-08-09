from abc import abstractmethod, ABC

from src.infra.helpers.model_object import ModelObject


class IClientRepository(ABC):
    @abstractmethod
    def create_client(self, **kwargs) -> ModelObject:
        raise NotImplementedError()
