from sqlalchemy import create_engine
from .dbutils import dbUtils
import pymysql

class DatabaseConnection:

    def __init__(self):
        self.dbUtils = dbUtils()
        self.host = self.dbUtils.get_host()
        self.pwd  = self.dbUtils.get_pwd()
        self.user = self.dbUtils.get_user()
        self.db   = self.dbUtils.get_db_name()
        self.engine = None


    def make_engine(self):
        '''
        Create and return the database connection
        '''
        self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.pwd}@{self.host}/{self.db}', echo=True, pool_pre_ping=True)
        return self.engine


    def make_connection(self):
        '''
        Establish the database connection once is created
        '''
        self.engine.connect()
