from __future__ import annotations

from abc import abstractmethod


class DatabaseModel:
    @property
    @abstractmethod
    def id(self) -> str:
        raise NotImplementedError()

    def __str__(self):
        return f"< {self.__class__.__name__}[{self.id}] >"

    def __repr__(self):
        pk = getattr(self, "id", None)
        pk_repr = f"[id={pk}]" if pk else ""

        return f"{self.__class__.__qualname__}({pk_repr})"

    def __eq__(self, other) -> bool:
        all_attr = vars(self)
        for key, value in all_attr.items():
            if not hasattr(other, key):
                return False

            if value != getattr(other, key):
                return False

        return True
