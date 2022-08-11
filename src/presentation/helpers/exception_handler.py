from src.domain.exceptions.api_error import APIError
from src.presentation.helpers.http_response import HttpResponse


class ExceptionHandler:

    def __init__(self):
        self.rest_exceptions = APIError

    def _create_error_dict(self, description: str = "Invalid", code: str = "INVALID") -> dict:
        return {"error": {"description": description, "code": code}}

    def handle(self, exception: Exception) -> HttpResponse:
        if not isinstance(exception, self.rest_exceptions):
            raise exception

        message = self._handle_message(exception)

        return HttpResponse(body=message, status_code=exception.status_code)

    def _handle_message(self, exception):
        if exception.raw:
            message = exception.raw
            message["code"] = exception.code
            return message

        if isinstance(exception.message, str):
            return self._create_error_dict(description=exception.message, code=exception.code)
