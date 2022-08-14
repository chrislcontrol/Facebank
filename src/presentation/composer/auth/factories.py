from src.domain.repositories.token_repository import TokenRepository
from src.domain.use_cases.authenticate.validate_token_use_case import ValidateTokenUseCase
from src.infra.repositories.postgres.postgres_token_repository import PostgresTokenRepository


def make_postgres_token_repository() -> TokenRepository:
    return PostgresTokenRepository()


def make_validate_token_use_case() -> ValidateTokenUseCase:
    return ValidateTokenUseCase(token_repository=make_postgres_token_repository())
