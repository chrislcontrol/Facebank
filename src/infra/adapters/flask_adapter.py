from src.presentation.controllers.interface.route import Controller
from src.presentation.helpers.exception_handler import ExceptionHandler
from src.presentation.helpers.http_request import HttpRequest


class FlaskAdapter:
    exception_handler = ExceptionHandler()

    def adapt(self, request: any, api_route: Controller):
        try:
            http_request = HttpRequest(
                headers=request.headers, body=request.json, params=request.args.to_dict()
            )
            response = api_route.route(http_request)
            return response

        except Exception as exc:
            return self.exception_handler.handle(exc)
