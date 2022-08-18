from src.domain.use_cases.user.create_user_use_case import CreateUserUseCase
from src.presentation.base.controller import Controller
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.helpers.http_response import HttpResponse
from src.presentation.security.authorization_classes.app_authentication import AppAuthentication


class CreateUserController(Controller):
    authentication_classes = [AppAuthentication]

    def __init__(self, create_user_use_case: CreateUserUseCase):
        self._create_user_use_case = create_user_use_case

    def route(self, *, http_request: HttpRequest) -> HttpResponse:
        # schema = CreateUserInputSchema(http_request.body)
        # schema.is_valid(True)

        user = self._create_user_use_case.create(**http_request.body, client=http_request.client)

        return HttpResponse(body=user.to_dict(), status_code=201)
