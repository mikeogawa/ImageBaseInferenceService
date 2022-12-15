from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .const import DB

DB_NAME = DB.DB_NAME
DB_USERNAME = DB.DB_USERNAME
DB_PASSWORD = DB.DB_PASSWORD
DB_ENDPOINT = DB.DB_ENDPOINT
DB_PORT = DB.DB_PORT
ALEMBIC_DB_NAME = DB.ALEMBIC_DB_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionDB = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@contextmanager
def SessionContext():
    db = SessionDB()
    try:
        yield db
    finally:
        db.close()
