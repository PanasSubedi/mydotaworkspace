import pymysql
from sqlalchemy import create_engine, MetaData, Table

def get_table(table_name, engine, metadata):
    return Table(table_name, metadata, autoload=True, autoload_with=engine)

def init_connection(database, db_host='127.0.0.1', username='root', password=''):

    CONN_STR = 'mysql+pymysql://{}:{}@{}/{}'.format(username, password, db_host, database)
    engine = create_engine(CONN_STR, echo=True)
    metadata = MetaData()

    return engine, metadata
