from typing import Dict

from src.domain.exceptions.invalid_input import InvalidInput
from src.presentation.serializers.types.base_field import BaseField, FailReason


class Serializer:
    def __init__(self, data: dict or list, many: bool = False):
        self.__data = data if many else [data]
        self.__many = many
        self.__validated_data = []
        self.__was_validated = False

    @property
    def validated_data(self) -> dict or list:
        if not self.__was_validated:
            raise Exception('You must call is_valid() before to access the validated data.')

        return self.__validated_data if self.__many or not self.__validated_data else self.__validated_data[0]

    @classmethod
    def fields(cls) -> Dict[str, BaseField]:
        return {key: value for key, value in vars(cls).items() if isinstance(value, BaseField)}

    def is_valid(self, raise_exception: bool = True) -> bool:
        errors = []
        valid_data = [{}]

        for validation_key, validation_value in self.fields().items():
            for index, data in enumerate(self.__data):
                input_value = data.get(validation_key)

                success, message = validation_value.validate(input_value)
                if success:
                    valid_data[index][validation_key] = input_value

                else:
                    errors.append(self._handle_fail(message=message,
                                                    field_name=validation_key,
                                                    base_field=validation_value))

        self.__validated_data = valid_data

        if errors:
            if raise_exception:
                raise InvalidInput(raw={"errors": list(set(errors))})
            return False
        self.__was_validated = True

        return True

    def _handle_fail(self, message, field_name: str, base_field: BaseField) -> dict:
        def error(message):
            return {"field": field_name, "description": message}

        if message == FailReason.INVALID_TYPE:
            return error(f"Expected {base_field.type.__qualname__} type.")

        if message == FailReason.REQUIRED_FIELD:
            return error("Is required.")

        if message == FailReason.MIN_LENGHT:
            return error(f"Ensure that field has at least {base_field.min_lenght} caracters.")

        if message == FailReason.MAX_LENGHT:
            return error(f"Ensure that field has less then {base_field.max_length} caracters.")

        return error("Unknow error.")
