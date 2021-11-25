from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine(
    'postgresql+psycopg2://user:password*@localhost:1234/database_name'
)
session = Session(engine)
Base = declarative_base()