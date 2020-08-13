from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# data will be stored in sqlite file named database
engine = create_engine('sqlite:///storage.db', echo=False)

Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def migrate():
    """
    generate required table and schemas for sql database
    required to be executed once in startup.
    """
    print("doing migration..")
    Base.metadata.create_all(engine)
