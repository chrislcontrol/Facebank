from flask import Blueprint, jsonify, request

from src.main.adapter.flask_adapter import FlaskAdapter
from src.presenters.composer.client.register_client_composer import register_client_composer

path = "/client"
api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route(path, methods=["POST"])
def create_client_route():
    adapter = FlaskAdapter()
    response = adapter.adapt(request=request, api_route=register_client_composer())
    return jsonify(response.body), response.status_code
