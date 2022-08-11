from src.domain.exceptions.api_error import APIError


class ObjectNotFound(APIError):
    DEFAULT_MESSAGE = "Object not found."
    DEFAULT_STATUS_CODE = 404
