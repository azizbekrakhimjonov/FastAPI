from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

BASE = "postgresql://postgres:postgresql@localhost/FastAPI"
engine = create_engine(BASE)
Session = sessionmaker(autoflush=False, autocommit=True, bind=engine)
Base = declarative_base()
