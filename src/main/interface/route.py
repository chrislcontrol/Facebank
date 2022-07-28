from typing import Type
from abc import ABC, abstractmethod
from src.presenters.utils.http_request import HttpRequest


class IRoute(ABC):
    """ Interface to Routes """

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]):
        """ Defining Route """

        raise NotImplementedError("Should implement method: route")
