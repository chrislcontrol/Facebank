from typing import List, Optional, Type

from src.domain.types.entity import Entity
from src.infra.repositories.object_values.model_object import ModelObject
from src.utils.objects import serialize_object


class Repository:
    entity = None

    def convert(self, obj: ModelObject, entity: Type[Entity] = None) -> Optional[entity]:
        if not self.entity:
            raise NotImplementedError("Must implement entity.")

        if not obj:
            return None
        entity = entity or self.entity
        return entity(**serialize_object(obj))  # noqa

    def convert_list(self, obj_list: List[ModelObject]) -> List[entity]:
        return list(map(lambda item: self.convert(item), obj_list))
