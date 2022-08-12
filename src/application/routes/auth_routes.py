from flask import request

from src.application.types.view import View
from src.presentation.composer.auth.authenticate_client_composer import authenticate_client_composer


class AuthenticateClientRoute(View):
    def post(self):
        return self.adapter.adapt(request=request, controller=authenticate_client_composer())
