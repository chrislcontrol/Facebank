from src.domain.exceptions.api_error import APIError


class InvalidPassword(APIError):
    DEFAULT_MESSAGE = "Invalid password."
    DEFAULT_STATUS_CODE = 403
