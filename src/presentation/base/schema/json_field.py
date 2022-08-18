from enum import Enum

from src.presentation.base.schema.base_field import FailReason, SuccessMessage
from src.presentation.base.schema.base_field_protocol import BaseFieldProtocol


class JSONField(BaseFieldProtocol):
    def validate(self, value: any) -> (bool, Enum):
        if not isinstance(value, dict):
            return False, FailReason.INVALID_TYPE

        return True, SuccessMessage.SUCCESS
