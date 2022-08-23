from src.domain.use_cases.authenticate.validate_token_use_case import ValidateTokenUseCase
from src.infra.database.db_connection_handler import DBHandler
from src.infra.database.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler
from src.infra.repositories.postgres.postgres_token_repository import PostgresTokenRepository


def validate_token_use_case_composer(db: DBHandler) -> ValidateTokenUseCase:
    repository = PostgresTokenRepository(db=db)
    return ValidateTokenUseCase(token_repository=repository)
