from src.domain.use_cases.authenticate.authenticate_client_use_case import IAuthenticateClientUseCase
from src.main.interface.route import IRoute
from src.presenters.serializers.authenticate.authenticate_client_serializer import AuthenticateClientSerializer
from src.presenters.utils.http_request import HttpRequest
from src.presenters.utils.http_response import HttpResponse


class AuthenticateClientController(IRoute):
    def __init__(self, authenticate_client_use_case: IAuthenticateClientUseCase):
        self._authenticate_client_use_case = authenticate_client_use_case

    def route(self, http_request: HttpRequest) -> HttpResponse:
        serializer = AuthenticateClientSerializer(data=http_request.body)
        token = self._authenticate_client_use_case.authenticate(input_data=serializer)

        return HttpResponse(status_code=200, body={"access_token": token.token})
