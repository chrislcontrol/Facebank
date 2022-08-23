from typing import Type


class OutputField:
    def __init__(self, *, source: str = None, type: Type):
        self.source = source
        self.type = type
