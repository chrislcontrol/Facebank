from dataclasses import dataclass, field

from src.domain.entities.client import Client
from src.domain.helpers.typed_class import TypedClass
from src.infra.database.db_connection_handler import DBHandler
from src.presentation.objects.headers import Headers


@dataclass(frozen=True)
class HttpRequest(TypedClass):
    headers: Headers
    db: DBHandler
    body: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)
    client: Client = None

    def __repr__(self):
        return (
            f"{self.__class__.__qualname__} (headers={self.headers}, body={self.body}, params={self.params})"
        )
