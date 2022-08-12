from flask import request

from src.application.types.view import View
from src.presentation.composer.client.register_client_composer import register_client_composer


class ClientRoute(View):
    def post(self):
        return self.adapter.adapt(request=request, controller=register_client_composer())
