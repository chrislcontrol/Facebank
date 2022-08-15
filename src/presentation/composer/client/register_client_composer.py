from src.domain.use_cases.client.register_client_use_case import RegisterClientUseCase
from src.infra.adapters.bcrypt_adapter import BcryptAdapter
from src.infra.adapters.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler
from src.infra.repositories.postgres.postgres_client_repository import PostgresClientRepository
from src.presentation.controllers.client.register_client_controller import RegisterClientController


def register_client_composer() -> RegisterClientController:
    db_connection_handler = SQLAlchemyConnectionHandler()
    repository = PostgresClientRepository(db_connection_handler=db_connection_handler)
    encryptor = BcryptAdapter()
    use_case = RegisterClientUseCase(client_repository=repository, encryptor=encryptor)
    return RegisterClientController(register_client_use_case=use_case)
