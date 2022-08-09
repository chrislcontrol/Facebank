from src.main.interface.route import IRoute
from src.presenters.utils.exception_handler import ExceptionHandler
from src.presenters.utils.http_request import HttpRequest


class FlaskAdapter:
    exception_handler = ExceptionHandler()

    def adapt(self, request: any, api_route: IRoute):
        try:
            http_request = HttpRequest(
                headers=request.headers, body=request.json, params=request.args.to_dict()
            )
            response = api_route.route(http_request)
            return response

        except Exception as exc:
            return self.exception_handler.handle(exc)
