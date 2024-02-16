import os

from sqlalchemy import (TIMESTAMP, Column, ForeignKeyConstraint,MetaData,String,Table,Text,create_engine, DateTime,Integer,text)
from core.infrastructure.mock import mock_data
metadata = MetaData()



user_table = Table(
    'user', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('email', String(100), nullable=False),
    Column('password', String(255), nullable=False),
    
    Column('created_at', TIMESTAMP,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('updated_at', DateTime, nullable=True),
    Column('deleted_at', DateTime, nullable=True),
)







account_table = Table(
    'account', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('balance', String(100), nullable=False),
    Column('secuencial', String(100), nullable=False),
    Column('city', String(100), nullable=False),
    Column('state', String(100), nullable=False),
    Column('address', String(100), nullable=False),
    Column('created_at', TIMESTAMP,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('updated_at', DateTime, nullable=True),
    Column('deleted_at', DateTime, nullable=True),
        ForeignKeyConstraint(['user_id'], ['user.id']),

)







    
transaction_table = Table(
    'transaction', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('account_id', String(100), nullable=False),
    Column('amount', String(100), nullable=False),
    Column('type', String(100), nullable=False),
    Column('created_at', TIMESTAMP,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('updated_at', DateTime, nullable=True),
    Column('deleted_at', DateTime, nullable=True),
    Column('size_screen', String(100), nullable=False),
    Column('os', String(100), nullable=False),
    Column('browser', String(100), nullable=False),
    Column('device', String(100), nullable=False),
    Column('ip', String(100), nullable=False),
)


audit_table = Table(
    'audit', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('user_id', String(100), nullable=False),
    Column('action', String(100), nullable=False),
    Column('path', String(100), nullable=False),
    Column('element', String(100), nullable=False),
    Column('os', String(100), nullable=False),
    Column('browser', String(100), nullable=False),
    Column('device', String(100), nullable=False),
    Column('size_screen', String(100), nullable=False),
    Column('created_at', TIMESTAMP,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('updated_at', DateTime, nullable=True),
    Column('deleted_at', DateTime, nullable=True),
)


def init_db_engine(db_uri=None):
    uri = db_uri or os.getenv('DB_URI')
    print(uri)
    db_engine = create_engine(uri)
    __create_tables_if_not_exists(db_engine)
    return db_engine


def db_connect(db_engine):
    return db_engine.connect()


def close_db_connection(db_connection):
    try:
        db_connection.close()
    except:
        pass


def __create_tables_if_not_exists(db_engine):
    # NOTE:  use Alembic for migrations (https://alembic.sqlalchemy.org/en/latest/)
    user_table.create(db_engine, checkfirst=True)
    account_table.create(db_engine, checkfirst=True)
    transaction_table.create(db_engine, checkfirst=True)
    audit_table.create(db_engine, checkfirst=True)
    
    mock_data(user_table, account_table, db_connect(db_engine))
