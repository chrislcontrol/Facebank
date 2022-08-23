from flask import request

from src.application.types.view import SessionView
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.composer.auth.authenticate_client_composer import authenticate_client_composer


class AuthenticateClientRoute(SessionView):
    def post(self, db: DBHandler):
        return self.adapter.adapt(request=request, controller=authenticate_client_composer(db=db), db=db)
