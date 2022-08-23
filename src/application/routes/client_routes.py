from flask import request

from src.application.types.view import SessionView
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.composer.client.register_client_composer import register_client_composer


class ClientRoute(SessionView):
    def post(self, db: DBHandler):
        return self.adapter.adapt(request=request, controller=register_client_composer(db=db), db=db)
