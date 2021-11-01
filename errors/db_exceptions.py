from fastapi import HTTPException
from sqlalchemy.exc import *
from util.file_readers.yaml_reader import yamlReader
import os,sys
configParams=yamlReader(os.path.dirname(os.path.realpath(__file__)) + '/../constants/db_error_messages.yaml')
def db_exceptions(e):
    if type(e).__name__=='DatabaseError':
        return HTTPException(status_code=404, detail=configParams['DatabaseError'])
    elif type(e).__name__=='InternalError':
        return HTTPException(status_code=503, detail=configParams['InternalError'])
    elif type(e).__name__=='NotSupportedError':
        return HTTPException(status_code=403, detail=configParams['NotSupportedError'])
    elif type(e).__name__=='SQLAlchemyError':
        return HTTPException(status_code=403, detail=configParams['sqlAlchemyError'])
    elif type(e).__name__=='NoSuchTableError':
        return HTTPException(status_code=404, detail=configParams['NoSuchTableError'])
    elif type(e).__name__=='DataError':
        return HTTPException(status_code=400, detail=configParams['DataError'])
    elif type(e).__name__=='IntegrityError':
        return HTTPException(status_code=400, detail=configParams['IntegrityError'])
    elif type(e).__name__=='OperationalError':
        return HTTPException(status_code=500, detail=configParams['OperationalError'])
    else:
        return HTTPException(status_code=500, detail=configParams['InternalServerError'])


