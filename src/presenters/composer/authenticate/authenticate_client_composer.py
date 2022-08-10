from src.data.authenticate.use_cases.authenticate_client_use_case import AuthenticateClientUseCase
from src.infra.adapters.encryptor import Encryptor
from src.infra.repositories.client_repository import ClientRepository
from src.infra.repositories.token_repository import TokenRepository
from src.presenters.controllers.authenticate.authenticate_client_controller import AuthenticateClientController


def authenticate_client_composer() -> AuthenticateClientController:
    client_repository = ClientRepository()
    token_repository = TokenRepository()
    encryptor = Encryptor()
    authenticate_client_use_case = AuthenticateClientUseCase(client_repository=client_repository,
                                                             token_repository=token_repository,
                                                             encryptor=encryptor)
    return AuthenticateClientController(authenticate_client_use_case=authenticate_client_use_case)
