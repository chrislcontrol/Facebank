from src.domain.use_cases.user.create_user_use_case import CreateUserUseCase
from src.presentation.base.controller import Controller
from src.presentation.controllers.helpers.http_request import HttpRequest
from src.presentation.controllers.helpers.http_response import HttpResponse
from src.presentation.schemas.user.create_user_input_schema import CreateUserInputSchema
from src.presentation.schemas.user.create_user_output_schema import CreateUserOutputSchema
from src.presentation.security.authorization_classes.app_authentication import AppAuthentication


class CreateUserController(Controller):
    authentication_classes = [AppAuthentication]
    input_schema = CreateUserInputSchema
    output_schema = CreateUserOutputSchema()

    def __init__(self, create_user_use_case: CreateUserUseCase):
        self._create_user_use_case = create_user_use_case

    def route(self, *, http_request: HttpRequest) -> HttpResponse:
        schema = self.input_schema(http_request.body)
        schema.is_valid(True)

        user = self._create_user_use_case.create(**schema.validated_data, client=http_request.client)

        return HttpResponse(body=self.output_schema.serialize_data(user), status_code=201)
