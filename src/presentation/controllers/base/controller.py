from abc import ABC, abstractmethod

from src.domain.exceptions.invalid_credentials import InvalidCredentials
from src.domain.exceptions.not_authenticated import AuthenticationNotProvided
from src.infra.database.database_model import DatabaseModel
from src.infra.repositories.base.repository import Repository
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

        return self.__middleware(attr)

    def __middleware(self, method):
        def run_authentications(http_request: HttpRequest, kwargs: dict):
            results = []
            for authentication in self.authentication_classes:
                auth_class = authentication()
                result = auth_class.authenticate(http_request, self)
                results.append(result)

            filter_by_client = list(filter(lambda i: isinstance(i, DatabaseModel), results))

            if not filter_by_client:
                if False in results:
                    raise InvalidCredentials()
                else:
                    raise AuthenticationNotProvided()

            serialized = serialize_object(http_request)
            serialized['client'] = filter_by_client[0]
            new_http_request = HttpRequest(**serialized)
            kwargs['http_request'] = new_http_request

        def lambda_func(*args, **kwargs):
            http_request: HttpRequest = kwargs['http_request']

            if self.authentication_classes:
                run_authentications(http_request=http_request, kwargs=kwargs)

            response = method(*args, **kwargs)

            return response

        return lambda_func
