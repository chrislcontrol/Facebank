from abc import ABC, abstractmethod
from typing import Union, Type

from src.domain.entities.client import Client
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.controllers.helpers.http_request import HttpRequest


class BaseAuthentication(ABC):
    db: DBHandler = None

    @abstractmethod
    def authenticate(self, http_request: HttpRequest, controller) -> Union[Client, bool, Type[None]]:
        raise NotImplementedError()
