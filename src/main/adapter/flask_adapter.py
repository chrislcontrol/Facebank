from src.main.interface.route import IRoute
from src.presenters.utils.http_request import HttpRequest


class FlaskAdapter:
    def adapt(self, request: any, api_route: IRoute):
        http_request = HttpRequest(
            headers=request.headers, body=request.json, params=request.args.to_dict()
        )
        response = api_route.route(http_request)
        return response
