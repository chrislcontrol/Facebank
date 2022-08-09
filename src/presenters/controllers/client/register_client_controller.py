from src.data.client.use_cases.register_client_use_case import RegisterClientUseCase
from src.main.interface.route import IRoute
from src.presenters.serializers.client.register_client_serializer import RegisterClientSerializer
from src.presenters.utils.http_request import HttpRequest
from src.presenters.utils.http_response import HttpResponse


class RegisterClientController(IRoute):
    def __init__(self, register_client_use_case: RegisterClientUseCase):
        self._register_client_use_case = register_client_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        serializer = RegisterClientSerializer(data=http_request.body)
        client = self._register_client_use_case.register(input_data=serializer)

        return HttpResponse(status_code=201, body=client.to_dict())
