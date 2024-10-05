# database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database (or use your own DB connection string)
engine = create_engine('sqlite:///groups.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define the Group model
class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True)
    username = Column(String)

# Create the tables in the database
Base.metadata.create_all(engine)
