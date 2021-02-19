from sqlalchemy import create_engine
from db.utils import dbUtils
import pymysql

class DatabaseConnection:

    def __init__(self):
        self.host = dbUtils.get_host()
        self.pwd  = dbUtils.get_pwd()
        self.user = dbUtils.get_user()
        self.db   = dbUtils.get_db_name()
        self.engine = None


    def make_engine(self):
        '''
        Create and return the database connection
        '''
        self.engine = create_engine(f'mysql://{self.user}:{self.pwd}@{self.host}/{self.db}', echo=True, pool_pre_ping=True)
        return self.engine


    def make_connection(self):
        '''
        Establish the database connection once is created
        '''
        self.engine.connect()
