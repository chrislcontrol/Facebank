from src.presenters.utils.exceptions import ObjectAlreadyExists


class ClientAlreadyExists(ObjectAlreadyExists):
    DEFAULT_MESSAGE = "Client already exists."
