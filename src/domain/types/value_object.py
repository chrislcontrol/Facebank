from abc import ABC


class ValueObject(ABC):
    def validate(self):
        raise NotImplementedError()
