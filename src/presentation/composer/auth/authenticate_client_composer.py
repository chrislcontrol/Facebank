from src.domain.use_cases.authenticate.authenticate_client_use_case import AuthenticateClientUseCase
from src.infra.adapters.bcrypt_adapter import BcryptAdapter
from src.infra.adapters.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler
from src.infra.repositories.postgres.postgres_client_repository import PostgresClientRepository
from src.infra.repositories.postgres.postgres_token_repository import PostgresTokenRepository
from src.presentation.controllers.authenticate.authenticate_client_controller import AuthenticateClientController


def authenticate_client_composer() -> AuthenticateClientController:
    db_connection_handler = SQLAlchemyConnectionHandler()
    client_repository = PostgresClientRepository(db_connection_handler=db_connection_handler)
    token_repository = PostgresTokenRepository(db_connection_handler=db_connection_handler)
    encryptor = BcryptAdapter()
    authenticate_client_use_case = AuthenticateClientUseCase(client_repository=client_repository,
                                                             token_repository=token_repository,
                                                             encryptor=encryptor)
    return AuthenticateClientController(authenticate_client_use_case=authenticate_client_use_case)
