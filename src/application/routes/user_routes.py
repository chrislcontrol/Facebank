from flask import request

from src.application.types.view import SessionView
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.composer.user.create_user_composer import create_user_composer


class UserRoute(SessionView):
    def post(self, db: DBHandler):
        return self.adapter.adapt(request=request, controller=create_user_composer(db=db), db=db)
