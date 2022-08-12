from flask import Request, jsonify

from src.infra.adapters.interface.app_adapter import AppAdapter
from src.presentation.controllers.interface.controller import Controller
from src.presentation.helpers.exception_handler import ExceptionHandler
from src.presentation.helpers.http_request import HttpRequest


class FlaskAdapter(AppAdapter):
    exception_handler = ExceptionHandler()

    def adapt(self, *, request: Request, controller: Controller) -> tuple:
        response = None
        try:
            http_request = HttpRequest(
                headers=request.headers, body=request.json, params=request.args.to_dict()
            )
            response = controller.route(http_request)

        except Exception as exc:
            response = self.exception_handler.handle(exc)

        finally:
            if response:
                return jsonify(response.body), response.status_code
            else:
                return "Internal server error", 500
