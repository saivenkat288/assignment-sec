import sqlalchemy,os, json
from sqlalchemy import MetaData,event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import psycopg2
import traceback
import sys,os
from util.file_readers.yaml_reader import yamlReader
from config.config_reader import get_settings

config = yamlReader(os.path.dirname(os.path.realpath(__file__)) + '/../../config/db_config.yaml')

settings = get_settings()

config['user'] = settings.db_username
config['password'] = settings.db_password

try:
  print("Connecting to Database")
  database_connection = sqlalchemy.create_engine("postgresql+psycopg2://"+config['user']+":"+config['password']+"@"+config['host']+"/"+config['database'],connect_args={'options':'-csearch_path={}'.format(config['schema'])})
  SessionLocal = sessionmaker(bind=database_connection)
  Base = declarative_base()
  meta = MetaData(database_connection)
  print("Succesfully connected to database")
except:
  @event.listens_for(database_connection, "connect", insert=True)
  def set_current_schema(dbapi_connection, connection_record):

    print("db connection event triggered")

    cursor = dbapi_connection.cursor()

    cursor.execute('SET search_path TO {schema}'.format(schema=config['schema']))

    cursor.close()
  print(traceback.format_exc())