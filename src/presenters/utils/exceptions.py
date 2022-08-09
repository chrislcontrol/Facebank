import re
from typing import Optional


class APIError(Exception):
    DEFAULT_MESSAGE = "Invalid."
    DEFAULT_STATUS_CODE = 400
    DEFAULT_CODE = None

    @property
    def _code(self) -> Optional[str]:
        class_name = self.__class__.__name__
        if class_name == "NixCoreValidationError":
            return None
        pattern = re.compile(r'(?<!^)(?=[A-Z])')
        name = pattern.sub('_', class_name).upper()

        return name

    def __init__(self, message: str = DEFAULT_MESSAGE,
                 status_code: int = DEFAULT_STATUS_CODE,
                 code: str = DEFAULT_CODE,
                 raw: any = {}):
        self.message = message if not raw else raw
        self.status_code = status_code
        self.code = code or self._code
        self.raw = raw

        super().__init__(str(self.message))


class InvalidInput(APIError):
    DEFAULT_MESSAGE = "Invalid input."
