from abc import ABC
from typing import Any

from src.infra.database.db_connection_handler import DBHandler
from src.presentation.base.controller import Controller


class AppAdapter(ABC):
    def adapt(self, *, request: Any, controller: Controller, db: DBHandler) -> tuple:
        raise NotImplementedError()
