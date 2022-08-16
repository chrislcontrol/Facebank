from src.infra.adapters.sql_alchemy.sql_alchemy_connection_handler import SQLAlchemyConnectionHandler


def composer(func):
    def lambda_func(*args, **kwargs):
        db_connection_handler = SQLAlchemyConnectionHandler()
        return func(db_connection_handler, *args, **kwargs)

    return lambda_func
