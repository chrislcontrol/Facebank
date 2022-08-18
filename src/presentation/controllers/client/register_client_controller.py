from src.domain.use_cases.client.register_client_use_case import RegisterClientUseCase
from src.presentation.base.controller import Controller
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.helpers.http_response import HttpResponse
from src.presentation.security.authorization_classes.app_authentication import AppAuthentication
from src.presentation.schemas.client.register_client_input_schema import RegisterClientInputSchema


class RegisterClientController(Controller):
    authentication_classes = [AppAuthentication]

    def __init__(self, register_client_use_case: RegisterClientUseCase):
        self._register_client_use_case = register_client_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        serializer = RegisterClientInputSchema(data=http_request.body)
        serializer.is_valid(True)
        client = self._register_client_use_case.register(**serializer.validated_data)

        return HttpResponse(status_code=201, body=client.to_dict())
