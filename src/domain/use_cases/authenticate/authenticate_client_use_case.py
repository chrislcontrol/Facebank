from src.domain.entities.token import Token
from src.presenters.serializers.authenticate.authenticate_client_serializer import AuthenticateClientSerializer


class IAuthenticateClientUseCase:
    def authenticate(self, *, input_data: AuthenticateClientSerializer) -> Token:
        raise NotImplementedError()
