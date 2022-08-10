from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Entity:
    id: str
    created: datetime
    modified: datetime

    def to_dict(self) -> dict:
        new_dict = {}
        for key, value in vars(self).copy().items():
            if not key.startswith('_'):
                if isinstance(value, (date, datetime)):
                    value = value.isoformat()

                new_dict[key] = value

        return new_dict
