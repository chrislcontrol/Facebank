from operator import itemgetter
from typing import Union, Type

from src.domain.entities.client import Client
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.base.controller import Controller
from src.presentation.composer.auth.validate_token_use_case_composer import validate_token_use_case_composer
from src.presentation.controllers.helpers.http_request import HttpRequest
from src.presentation.security.helpers.base_authentication import BaseAuthentication


class AppAuthentication(BaseAuthentication):
    def __init__(self, db: DBHandler):
        self.db = db
        self.validate_token_use_case = validate_token_use_case_composer(db=self.db)

    def authenticate(self, http_request: HttpRequest, controller: Controller) -> Union[Client, bool, Type[None]]:
        authorization = http_request.headers.authorization
        if not authorization.value:
            return None

        validated = self.validate_token_use_case.validate(token_string=authorization)
        token, client, success = itemgetter("token", "client", "success")(validated)

        if not success:
            return False

        return client
