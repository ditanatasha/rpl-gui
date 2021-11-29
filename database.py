from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib
from urllib import parse
import os
import sqlalchemy
from sqlalchemy.sql.expression import null
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey,Date
from sqlalchemy.orm import relationship

host_server = os.environ.get('host_server', 'fastapi-server.postgres.database.azure.com')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'rpl')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'fastapiadmin@fastapi-server')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'Rpl12345')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

database = DATABASE_URL

metadata = sqlalchemy.MetaData()

engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine)
db = SessionLocal()



