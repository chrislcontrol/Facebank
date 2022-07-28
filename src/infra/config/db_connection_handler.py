from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main.environments.variables import DATABASE_URL


class DBConnectionHandler:
    """ Sqlalchemy database connection """

    def __init__(self):
        self.__connection_string = DATABASE_URL
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        from src.infra.config.database import Base

        engine = create_engine(self.__connection_string)
        Base.metadata.create_all(engine)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
