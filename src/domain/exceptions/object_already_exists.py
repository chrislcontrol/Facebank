from src.domain.exceptions.api_error import APIError


class ObjectAlreadyExists(APIError):
    DEFAULT_MESSAGE = "Object already exists."
    DEFAULT_STATUS_CODE = 409
