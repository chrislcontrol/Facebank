from src.domain.use_cases.authenticate.authenticate_client_use_case import AuthenticateClientUseCase
from src.infra.adapters.bcrypt_adapter import BcryptAdapter
from src.infra.repositories.sql_alchemy.postgres.postgres_client_repository import PostgresClientRepository
from src.infra.repositories.sql_alchemy.postgres.postgres_token_repository import PostgresTokenRepository
from src.presentation.controllers.authenticate.authenticate_client_controller import AuthenticateClientController


def authenticate_client_composer() -> AuthenticateClientController:
    client_repository = PostgresClientRepository()
    token_repository = PostgresTokenRepository()
    encryptor = BcryptAdapter()
    authenticate_client_use_case = AuthenticateClientUseCase(client_repository=client_repository,
                                                             token_repository=token_repository,
                                                             encryptor=encryptor)
    return AuthenticateClientController(authenticate_client_use_case=authenticate_client_use_case)
