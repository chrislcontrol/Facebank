from abc import ABC, abstractmethod

from src.domain.entities.client import Client
from src.domain.exceptions.invalid_credentials import InvalidCredentials
from src.domain.exceptions.not_authenticated import AuthenticationNotProvided
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.helpers.http_response import HttpResponse
from src.utils.objects import serialize_object


class Controller(ABC):
    authentication_classes = []

    @abstractmethod
    def route(self, *, http_request: HttpRequest) -> HttpResponse:
        raise NotImplementedError("Should implement method: route")

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if name != "route":
            return attr

        return self.__run_authentications(attr)

    def __run_authentications(self, method):
        def lambda_func(*args, **kwargs):
            http_request: HttpRequest = kwargs['http_request']

            results = []
            for authentication in self.authentication_classes:
                auth_class = authentication()
                result = auth_class.authenticate(http_request, self)
                results.append(result)

            filter_by_client = list(filter(lambda i: isinstance(i, Client), results))

            if not filter_by_client:
                if False in results:
                    raise InvalidCredentials()
                else:
                    raise AuthenticationNotProvided()

            serialized = serialize_object(http_request)
            serialized['client'] = filter_by_client[0]
            new_http_request = HttpRequest(**serialized)
            kwargs['http_request'] = new_http_request

            return method(*args, **kwargs)

        return lambda_func
