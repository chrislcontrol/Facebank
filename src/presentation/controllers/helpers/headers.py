from dataclasses import dataclass

from src.domain.types.token import AuthorizationToken


@dataclass(frozen=True)
class Headers:
    environ: dict
    provided: dict

    @property
    def authorization(self) -> AuthorizationToken:
        return AuthorizationToken(self.provided.get("AUTHORIZATION"))
