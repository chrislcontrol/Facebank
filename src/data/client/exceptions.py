from src.presenters.utils.exceptions import ObjectAlreadyExists, ObjectNotFound


class ClientAlreadyExists(ObjectAlreadyExists):
    DEFAULT_MESSAGE = "Client already exists."


class ClientNotFound(ObjectNotFound):
    DEFAULT_MESSAGE = "Client not found."
