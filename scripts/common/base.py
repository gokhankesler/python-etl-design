from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine(
    'postgresql+psycopg2://postgres:password@localhost:1234/postgres'
)
session = Session(engine)
Base = declarative_base()