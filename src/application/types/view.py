from flask.views import MethodView

from src.infra.adapters.flask_adapter import FlaskAdapter
from src.infra.database.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler
from src.utils.http_methods import HttpMethods


class SessionView(MethodView):
    adapter = FlaskAdapter()

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if name.lower() not in HttpMethods.all() or not callable(attr):
            return attr

        def middleware(*args, **kwargs):
            with SQLAlchemyConnectionHandler() as db_handler:
                result = attr(*args, **kwargs, db=db_handler)
                return result

        return middleware
