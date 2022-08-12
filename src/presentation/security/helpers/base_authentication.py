from abc import ABC, abstractmethod
from typing import Union, Type

from src.domain.entities.client import Client
from src.presentation.helpers.http_request import HttpRequest


class BaseAuthentication(ABC):
    @abstractmethod
    def authenticate(self, http_request: HttpRequest, controller) -> Union[Client, bool, Type[None]]:
        raise NotImplementedError()
