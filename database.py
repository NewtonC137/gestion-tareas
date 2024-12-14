from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task

DATABASE_URL = "sqlite:///tasks.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
   return Session()