from typing import Dict

from src.domain.types.entity import Entity


class JoinQueryset:
    def __init__(self, *, main: Entity, **joins: Dict[str, Entity]):
        self.main = main
        for key, value in joins.items():
            setattr(self, key, value)

    def exists(self) -> bool:
        return bool(self.main)
