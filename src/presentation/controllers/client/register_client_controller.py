from src.domain.use_cases.client.register_client_use_case import RegisterClientUseCase
from src.presentation.controllers.base.controller import Controller
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.helpers.http_response import HttpResponse
from src.presentation.security.authorization_classes.app_authentication import AppAuthentication
from src.presentation.serializers.client.register_client_serializer import RegisterClientSerializer


class RegisterClientController(Controller):
    authentication_classes = [AppAuthentication]

    def __init__(self, register_client_use_case: RegisterClientUseCase):
        self._register_client_use_case = register_client_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        serializer = RegisterClientSerializer(data=http_request.body)
        serializer.is_valid(True)
        client = self._register_client_use_case.register(**serializer.validated_data)

        return HttpResponse(status_code=201, body=client.to_dict())
