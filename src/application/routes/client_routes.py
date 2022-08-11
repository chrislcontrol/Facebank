from flask import jsonify, request
from flask.views import MethodView

from src.infra.adapters.flask_adapter import FlaskAdapter
from src.presentation.composer.client.register_client_composer import register_client_composer


class ClientRoute(MethodView):
    def post(self):
        adapter = FlaskAdapter()
        response = adapter.adapt(request=request, api_route=register_client_composer())
        return jsonify(response.body), response.status_code
