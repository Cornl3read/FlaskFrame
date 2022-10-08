from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine)
                            )
Base = declarative_base()
Base.query = db_session.query_property()


# initilize db instance in memory for testing and development
def init_db():
    import models
    Base.metadata.create_all(bind=engine)

