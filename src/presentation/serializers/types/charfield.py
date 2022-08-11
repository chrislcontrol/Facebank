from src.presentation.serializers.types.base_field import BaseField


class CharField(BaseField):
    def __init__(self, *,
                 min_lenght: int = 0,
                 max_length: int = 255,
                 required: bool = True):
        super().__init__(type=str, min_lenght=min_lenght, max_length=max_length, required=required)
