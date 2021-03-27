import sqlalchemy_utils
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.engine.url import URL


class DatabaseCore(object):
    def __init__(self, username, password, host, database_name):
        self.driver_name = 'postgresql'
        self.username = username
        self.password = password
        self.host = host
        self.database_name = database_name
        
        self.engine = self.get_engine_instance()

    def _get_database_config(self):
        return {'drivername': self.driver_name,
                'username': self.username,
                'password': self.password,
                'host': self.host}

    def _get_database_url(self):
        db_uri = URL(**self._get_database_config())

        return f'{db_uri}/{self.database_name}'

    def exist_database(self):
        return sqlalchemy_utils.database_exists(self._get_database_url())

    def create_database(self):
        return sqlalchemy_utils.create_database(self._get_database_url())

    def get_engine_instance(self):
        database_url = self._get_database_url()

        return create_engine(database_url)

    def create_table(self, name):
        metadata = MetaData()
        metadata.reflect(bind=self.get_engine_instance())

        tables = metadata.tables.keys()

        if name not in tables:
            table = Table(name, metadata,
                          Column('id', Integer, primary_key=True),
                          Column('key', String),
                          Column('val', Integer))

            table.create(self.get_engine_instance())
