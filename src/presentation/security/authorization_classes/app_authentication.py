from operator import itemgetter
from typing import Union, Type

from src.domain.entities.client import Client
from src.presentation.composer.auth.validate_token_use_case_composer import validate_token_use_case_composer
from src.presentation.controllers.base.controller import Controller
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.security.helpers.base_authentication import BaseAuthentication


class AppAuthentication(BaseAuthentication):
    validate_token_use_case = validate_token_use_case_composer()

    def authenticate(self, http_request: HttpRequest, controller: Controller) -> Union[Client, bool, Type[None]]:
        authorization = http_request.headers.authorization
        if not authorization:
            return None

        validated = self.validate_token_use_case.validate(token_string=authorization)
        token, client, success = itemgetter("token", "client", "success")(validated)

        if not success:
            return False

        return client
