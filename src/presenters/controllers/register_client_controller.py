from src.data.client.use_cases.register_client_use_case import RegisterClientUseCase
from src.main.interface.route import IRoute
from src.presenters.utils.http_request import HttpRequest
from src.presenters.utils.http_response import HttpResponse


class RegisterClientController(IRoute):
    def __init__(self, register_client_use_case: RegisterClientUseCase):
        self._register_client_use_case = register_client_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        client = self._register_client_use_case.register(**http_request.body)

        return HttpResponse(status_code=201, body={})


