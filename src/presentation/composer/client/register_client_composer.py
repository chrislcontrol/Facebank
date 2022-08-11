from src.domain.use_cases.client.register_client_use_case import RegisterClientUseCase
from src.infra.adapters.bcrypt_adapter import BcryptAdapter
from src.infra.repositories.postgres.postgres_client_repository import PostgresClientRepository
from src.presentation.controllers.client.register_client_controller import RegisterClientController


def register_client_composer() -> RegisterClientController:
    repository = PostgresClientRepository()
    encryptor = BcryptAdapter()
    use_case = RegisterClientUseCase(client_repository=repository, encryptor=encryptor)
    return RegisterClientController(register_client_use_case=use_case)
