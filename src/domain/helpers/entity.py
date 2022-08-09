from dataclasses import dataclass


@dataclass
class Entity:

    def to_dict(self) -> dict:
        return {key: value for key, value in vars(self).items() if not key.startswith('_')}
