import pymysql
from sqlalchemy import create_engine, MetaData, Table

class DBConn:

    def get(self, table_name, conditions):
        query = self._get(table_name, conditions)
        return query.fetchall()

    def is_present(self, table_name, conditions):
        query = self._get(table_name, conditions)
        return query.rowcount

    def _get(self, table_name, conditions):
        '''
            conditions = {
                'id': 1,
            }
        '''
        if table_name not in self.tables:
            raise Exception('add table to the db variable first using add_tables method')

        table = self.tables[table_name]
        query = table.select()

        for condition in conditions:
            query = query.where(getattr(table.c, condition)==conditions[condition])

        query = self.engine.execute(query)
        return query

    def insert(self, table_name, values):
        if table_name not in self.tables:
            raise Exception('add table to the db variable first using add_tables method')

        table = self.tables[table_name]
        insert_query = self.engine.execute(table.insert().values(values))
        return insert_query.lastrowid

    def add_tables(self, tables):
        assert type(tables) is list

        for table in tables:
            if table not in self.tables:
                self.tables[table] = Table(table, self.metadata, autoload=True, autoload_with=self.engine)

    def _init_connection(self, database_name, db_host='127.0.0.1', username='root', password=''):

        CONN_STR = 'mysql+pymysql://{}:{}@{}/{}'.format(username, password, db_host, database_name)
        engine = create_engine(CONN_STR, echo=True)
        metadata = MetaData()

        self.engine = engine
        self.metadata = metadata

    def __init__(self, database_name, **kwargs):
        self._init_connection(database_name, **kwargs)
        self.tables = {}
