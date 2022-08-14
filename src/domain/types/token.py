from dataclasses import dataclass
from typing import Optional

from src.domain.types.value_object import ValueObject


@dataclass(frozen=True)
class AuthorizationToken(ValueObject):
    value: str

    def validate(self) -> Optional[str]:
        if not self.value.startswith('Token '):
            return None
        return self.value
