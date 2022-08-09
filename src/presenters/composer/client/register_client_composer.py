from src.data.client.use_cases.register_client_use_case import RegisterClientUseCase
from src.infra.repositories.client_repository import ClientRepository
from src.presenters.controllers.client.register_client_controller import RegisterClientController


def register_client_composer() -> RegisterClientController:
    repository = ClientRepository()
    use_case = RegisterClientUseCase(client_repository=repository)
    return RegisterClientController(register_client_use_case=use_case)
