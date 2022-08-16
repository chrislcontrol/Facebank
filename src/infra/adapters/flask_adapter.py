from flask import Request, jsonify

from src.infra.base.app_adapter import AppAdapter
from src.presentation.base.controller import Controller
from src.presentation.helpers.exception_handler import ExceptionHandler
from src.presentation.helpers.http_request import HttpRequest
from src.presentation.objects.headers import Headers


class FlaskAdapter(AppAdapter):
    exception_handler = ExceptionHandler()

    def adapt(self, *, request: Request, controller: Controller) -> tuple:
        try:
            http_request = HttpRequest(
                headers=self.__convert_headers(request.headers),
                body=request.json,
                params=request.args.to_dict()
            )
            response = controller.route(http_request=http_request)

        except Exception as exc:
            response = self.exception_handler.handle(exc)

        if response:
            return jsonify(response.body), response.status_code
        else:
            return "Internal server error", 500

    def __convert_headers(self, flask_headers):
        environ_headers = flask_headers.environ
        provided_headers = flask_headers.to_wsgi_list()

        return Headers(provided={key.upper(): value for key, value in provided_headers},
                       environ=environ_headers)
