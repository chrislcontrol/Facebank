from src.domain.exceptions.object_already_exists import ObjectAlreadyExists


class ClientAlreadyExists(ObjectAlreadyExists):
    DEFAULT_MESSAGE = "Client already exists."
