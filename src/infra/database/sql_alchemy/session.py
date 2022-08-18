from sqlalchemy import create_engine
from sqlalchemy.future import engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from src.infra.environments.variables import DATABASE_URL


def create_session():
    base = declarative_base()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    base.query = db_session.query_property()
    new_engine = create_engine(DATABASE_URL)
    base.metadata.create_all(new_engine)
    session_maker = sessionmaker()
    return session_maker(bind=new_engine)
