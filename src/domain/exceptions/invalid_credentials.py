from src.domain.exceptions.api_error import APIError


class InvalidCredentials(APIError):
    DEFAULT_MESSAGE = "Invalid credentials."
    DEFAULT_STATUS_CODE = 403
