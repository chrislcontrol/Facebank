from flask import jsonify, request
from flask.views import MethodView

from src.infra.adapters.flask_adapter import FlaskAdapter
from src.presentation.composer.auth.authenticate_client_composer import authenticate_client_composer


class AuthenticateClientRoute(MethodView):
    def post(self):
        adapter = FlaskAdapter()
        response = adapter.adapt(request=request, api_route=authenticate_client_composer())
        return jsonify(response.body), response.status_code
