from sqlalchemy import create_engine
from sqlalchemy.future import engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from src.application.environments.variables import DATABASE_URL

Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()


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
        engine = create_engine(self.__connection_string)
        Base.metadata.create_all(engine)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member