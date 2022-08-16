from src.domain.exceptions.api_error import APIError


class UserAlreadyExists(APIError):
    DEFAULT_MESSAGE = "User's username must be unique."
    DEFAULT_STATUS_CODE = 409
