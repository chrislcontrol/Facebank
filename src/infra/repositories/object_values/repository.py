from typing import List

from src.infra.repositories.object_values.model_object import ModelObject


class Repository:
    entity = ModelObject

    def convert(self, obj: object) -> entity:
        if not obj:
            return None
        return ModelObject(**{key: value for key, value in vars(obj).items() if not key.startswith('_')})

    def convert_list(self, obj_list: List[object]) -> List[entity]:
        return list(map(lambda item: self.convert(item), obj_list))
