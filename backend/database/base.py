from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .connection import DatabaseConnection


# Establezco la coneccion a mi base de datos 
database = DatabaseConnection()
engine = database.make_engine()
database.make_connection()

Session = sessionmaker(bind=engine)

Base = declarative_base()

