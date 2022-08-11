from typing import Type
from abc import ABC, abstractmethod
from src.presentation.helpers.http_request import HttpRequest


class Controller(ABC):
    """ Interface to Routes """

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]):
        """ Defining Route """

        raise NotImplementedError("Should implement method: route")
