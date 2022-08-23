from typing import Any

from src.presentation.base.schema.base_field import BaseField


class JSONField(BaseField):
    def __init__(self, required: bool = True, default: Any = None):
        super().__init__(required=required, default=default, type=dict)
