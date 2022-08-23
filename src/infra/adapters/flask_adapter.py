from flask import Request, jsonify

from src.infra.base_classes.app_adapter import AppAdapter
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.base.controller import Controller
from src.presentation.controllers.helpers.exception_handler import ExceptionHandler
from src.presentation.controllers.helpers.headers import Headers
from src.presentation.controllers.helpers.http_request import HttpRequest


class FlaskAdapter(AppAdapter):
    exception_handler = ExceptionHandler()

    def adapt(self, *, request: Request, controller: Controller, db: DBHandler) -> tuple:
        try:
            http_request = HttpRequest(
                headers=self.__convert_headers(request.headers),
                body=request.json,
                params=request.args.to_dict(),
                db=db
            )
            response = controller.route(http_request=http_request)
            return jsonify(response.body), response.status_code

        except Exception as exc:
            response = self.exception_handler.handle(exc)
            return jsonify(response.body), response.status_code

    def __convert_headers(self, flask_headers):
        environ_headers = flask_headers.environ
        provided_headers = flask_headers.to_wsgi_list()

        return Headers(provided={key.upper(): value for key, value in provided_headers},
                       environ=environ_headers)
