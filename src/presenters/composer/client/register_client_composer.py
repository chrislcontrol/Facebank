from src.data.client.use_cases.register_client_use_case import RegisterClientUseCase
from src.infra.helpers.encryptor import Encryptor
from src.infra.repositories.client_repository import ClientRepository
from src.presenters.controllers.client.register_client_controller import RegisterClientController


def register_client_composer() -> RegisterClientController:
    repository = ClientRepository()
    encryptor = Encryptor()
    use_case = RegisterClientUseCase(client_repository=repository, encryptor=encryptor)
    return RegisterClientController(register_client_use_case=use_case)
