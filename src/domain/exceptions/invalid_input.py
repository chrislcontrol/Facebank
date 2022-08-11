from src.domain.exceptions.api_error import APIError


class InvalidInput(APIError):
    DEFAULT_MESSAGE = "Invalid input."
