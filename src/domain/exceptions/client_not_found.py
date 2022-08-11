from src.domain.exceptions.object_not_found import ObjectNotFound


class ClientNotFound(ObjectNotFound):
    DEFAULT_MESSAGE = "Client not found."
