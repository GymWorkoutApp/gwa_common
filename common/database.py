from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from common.settings import DatabaseConfig

engine = create_engine(DatabaseConfig.get_uri())

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


@contextmanager
def async_session() -> 'Session':
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
