from dataclasses import dataclass
from typing import Optional

from src.domain.types.value_object import ValueObject


@dataclass(frozen=True)
class AuthorizationToken(ValueObject):
    value: str

    def validate(self) -> str:
        if not self.value:
            return ""

        if not self.value.startswith('Token '):
            return ""
        return self.value

    def without_prefix(self, validate: bool = True) -> str:
        value = self.validate() if validate else self.value
        return value.split('Token ')[-1]
