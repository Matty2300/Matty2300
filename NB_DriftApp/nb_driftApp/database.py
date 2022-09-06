from importlib.metadata import metadata
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib




params = urllib.parse.quote_plus('DRIVER={SQL SERVER};SERVER=10.140.12.55;DATABASE=DriftSide;UID=DriftAdmin;PWD=Nbdrift1881')
engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
    
    


