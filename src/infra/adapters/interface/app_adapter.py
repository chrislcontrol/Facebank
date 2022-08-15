from abc import ABC
from typing import Any

from src.presentation.controllers.base.controller import Controller


class AppAdapter(ABC):
    def adapt(self, *, request: Any, controller: Controller):
        raise NotImplementedError()
