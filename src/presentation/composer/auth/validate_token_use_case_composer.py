from src.domain.use_cases.authenticate.validate_token_use_case import ValidateTokenUseCase
from src.infra.database.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler
from src.infra.repositories.postgres.postgres_token_repository import PostgresTokenRepository


def validate_token_use_case_composer() -> ValidateTokenUseCase:
    repository = PostgresTokenRepository()
    return ValidateTokenUseCase(token_repository=repository)
