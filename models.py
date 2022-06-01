from start_base import Base, engine
from sqlalchemy import Column, String, Integer


class Words(Base):
    __tablename__ = "WordTable"

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)


class Users2(Base):
    __tablename__ = "User_data"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


def start_tables():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
