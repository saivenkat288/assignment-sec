import sys,os,zlib,zipfile,shutil
import ast
from starlette import responses
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../")
from util.database.database_connection import database_connection,meta,SessionLocal
from datetime import datetime,date
import pandas as pd
from models.dbmodels.models import *
from sqlalchemy.exc import *
from sqlalchemy import and_
from sqlalchemy.schema import DropTable, CreateTable
from sqlalchemy import  Column,  Integer, String, Table,text,Float,Text,cast, Date
from sqlalchemy import create_engine,MetaData,Table,select,Column,and_
from sqlalchemy.sql.expression import literal
import numpy as np
import traceback
import json,glob
now = datetime.now() # current date and time
current_date_time = now.strftime("%m-%d-%Y %H:%M:%S")
import logging
from errors.db_exceptions import db_exceptions
import re
import bcrypt
from errors.traceback_exceptions import traceException
#from sqlalchemy_views import CreateView

regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
logging.basicConfig(filename="database_logs.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')

now = datetime.now()  # current date and time
current_date_time = now.strftime("%m-%d-%Y %H:%M:%S")
current_date = date.today().strftime("%m-%d-%Y")

logger = logging.getLogger()

class CrudOperations:
    def __init__(self):
        self.cursor = None
        self.pipeline_id=0

            
    def getUserByEmail(self,email):
        '''
        Function will return the email from the databse from user_details table
        '''
        try:
            self.cursor=SessionLocal()
            if re.fullmatch(regex,email):
                query1=self.cursor.query(UserDetails).filter(UserDetails.email==email).all()
                if len(query1)>0:
                    return query1[0]
                else:
                    return None
        except TypeError as te:
            return 'Email is not present'
        except Exception as e:
            db_exceptions(e)
            self.cursor.rollback()
            traceException(e)
            logger.error(e)

    def getUserPassword(self,email):
        '''
        Function will fetech the user password based on email id's
        '''
        try:
            self.cursor=SessionLocal()
            if re.fullmatch(regex,email):
                query1=self.cursor.query(UserDetails).filter(UserDetails.email==email).all()
                if len(query1)>0:
                    return query1[0].password
            else:
                return None
        except TypeError as te:
            return 'Email is not present'
        except TypeError as te:
            return 'Email is not present'
        except Exception as e:
            db_exceptions(e)
            self.cursor.rollback()
            traceException(e)
            logger.error(e)
    def insertAnswersToDB(self,df,table_name):
        try:
            df_columns = list(df.columns)
            dynamic_columns = []
            for col in df_columns:
                dt = df.dtypes[col]
                if dt == np.int64 :
                    dynamic_columns.append(Column(col, Integer))
                elif dt == np.object:
                    dynamic_columns.append(Column(col, Text))
                elif dt == np.float64:
                    dynamic_columns.append(Column(col, Float))
                else:
                    dynamic_columns.append(Column(col, Text))
            table = Table(table_name, meta, *dynamic_columns,extend_existing=True)
            #table.drop()
            table_creation_sql = CreateTable(table)
            database_connection.engine.execute(table_creation_sql)
            df.to_sql(table_name,con = database_connection,if_exists='replace',index=False)
        except Exception as e:
            db_exceptions(e)
            traceException(e)
            logger.error(e)

    def updateAnswersToDB(self):
        try:
            self.cursor=SessionLocal()
            if re.fullmatch(regex,email):
                query1=self.cursor.query(UserDetails).filter(UserDetails.email==email).all()
                if len(query1)>0:
                    return query1[0].password
            else:
                return None
        except TypeError as te:
            return 'Email is not present'
        except TypeError as te:
            return 'Email is not present'
        except Exception as e:
            db_exceptions(e)
            self.cursor.rollback()
            traceException(e)
            logger.error(e)

    def fetchAnswersFromDB(self,table_name):
        try:
            self.cursor=SessionLocal()
            res=database_connection.engine.execute('''SELECT * FROM "{}"'''.format(table_name)).fetchall()
            return res
        except TypeError as te:
            return 'Email is not present'
        except TypeError as te:
            return 'Email is not present'
        except Exception as e:
            db_exceptions(e)
            self.cursor.rollback()
            traceException(e)
            logger.error(e)