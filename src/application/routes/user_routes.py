from flask import request

from src.application.types.view import View
from src.presentation.composer.user.create_user_composer import create_user_composer


class UserRoute(View):
    def post(self):
        return self.adapter.adapt(request=request, controller=create_user_composer())
