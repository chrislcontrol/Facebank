from abc import ABC, abstractmethod

from src.presentation.helpers.http_request import HttpRequest
from src.presentation.helpers.http_response import HttpResponse


class Controller(ABC):
    """ Interface to Routes """

    @abstractmethod
    def route(self, http_request: HttpRequest) -> HttpResponse:
        """ Defining Route """

        raise NotImplementedError("Should implement method: route")
