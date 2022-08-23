from src.infra.database.db_connection_handler import DBHandler
from src.presentation.base.controller import Controller
from src.presentation.controllers.helpers import HttpRequest
from src.presentation.controllers.helpers import HttpResponse


class IControllerComposer(Controller):
    def __init__(self, db: DBHandler):  # noqa
        pass

    def route(self, *, http_request: HttpRequest) -> HttpResponse:
        pass
