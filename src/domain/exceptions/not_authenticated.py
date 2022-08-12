from src.domain.exceptions.api_error import APIError


class AuthenticationNotProvided(APIError):
    DEFAULT_MESSAGE = "Authentication credentials were not provided."
    DEFAULT_STATUS_CODE = 403
