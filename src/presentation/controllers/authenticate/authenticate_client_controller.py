from src.presentation.controllers.interface.route import Controller
from src.domain.use_cases.authenticate.authenticate_client_use_case import AuthenticateClientUseCase
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.helpers.http_response import HttpResponse
from src.presentation.serializers.authenticate.authenticate_client_serializer import AuthenticateClientSerializer


class AuthenticateClientController(Controller):
    def __init__(self, authenticate_client_use_case: AuthenticateClientUseCase):
        self._authenticate_client_use_case = authenticate_client_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        serializer = AuthenticateClientSerializer(data=http_request.body)
        serializer.is_valid(True)
        token = self._authenticate_client_use_case.authenticate(**serializer.validated_data)

        return HttpResponse(status_code=200, body={"access_token": token.token})
