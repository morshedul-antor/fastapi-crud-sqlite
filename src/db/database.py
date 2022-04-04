from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

