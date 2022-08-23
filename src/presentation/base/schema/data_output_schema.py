from typing import Any, Union

from src.domain.types.entity import Entity
from src.presentation.base.schema.output_field import OutputField


class OutputSchema:
    def __init__(self, source: str = None):
        self.source = source

    @classmethod
    def __get_from_dict(cls, data: dict, key: str, value: Union[OutputField, Any]) -> Any:
        key = value.source or key
        result = None
        for index, layer in enumerate(key.split('.')):
            result = data.get(layer) if index == 0 else result.get(layer, {})

        return result

    @classmethod
    def __get_from_entity(cls, entity: Entity, key: str, value: Union[OutputField, Any]) -> Any:
        key = value.source or key
        result = None
        for index, layer in enumerate(key.split('.')):
            result = getattr(entity, layer) if index == 0 else getattr(result, layer)

        if isinstance(value, OutputSchema):
            result = value.serialize_data(data=result)

        return result

    @classmethod
    def serialize_data(cls, data: Union[dict, Entity]) -> dict:
        output = {}
        for key, value in vars(cls).items():
            if isinstance(value, (OutputSchema, OutputField)):
                if isinstance(data, dict):
                    output[key] = cls.__get_from_dict(data=data, key=key, value=value)
                elif isinstance(data, Entity):
                    output[key] = cls.__get_from_entity(entity=data, key=key, value=value)

        return output
