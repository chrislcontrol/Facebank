from flask.views import MethodView

from src.infra.adapters.flask_adapter import FlaskAdapter


class View(MethodView):
    adapter = FlaskAdapter()
