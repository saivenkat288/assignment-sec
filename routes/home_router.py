from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy import *
import re 
from errors.db_exceptions import db_exceptions
import bcrypt
import traceback,sys,os
from models.httpmodels.input.request_models import *
from fastapi.routing import APIRouter
from util.database.dao_postgres import CrudOperations
from errors.traceback_exceptions import traceException
from io import BytesIO
from service.service import *
import requests
import pandas as pd
db_client=CrudOperations()
app = APIRouter()

@app.post('/user/signin',status_code=status.HTTP_200_OK,name="Login")
async def signIn(authParams:AuthParams):
    '''
    This API works for siginin
    email:str,password:str 
    '''

    try:    
        pass_email=  db_client.getUserByEmail(authParams.email)
        if pass_email:
            passwd=db_client.getUserPassword(pass_email.email)
            user_passwd = authParams.password.encode('utf8')
            system_passwd = passwd.encode('utf8')
            results= bcrypt.checkpw(user_passwd,system_passwd)
            print("pass_email",passwd)
            if results:
                return  {"status": 200, "message": "Login Success", "user_data":{
                    "email":authParams.email,
                    "name":pass_email.first_name+' '+pass_email.last_name,
                    
                    "id":pass_email.id
                }}
            else:
                return {"status": 200, "message": "Login Failed wrong password"}
        return {"status":200,"message":"Email is not valid"}
    
    except Exception as e:
        traceException(e)
        db_exceptions(e)

@app.post('/insert/answers/{section}',status_code=status.HTTP_200_OK,name="insert-answers")
async def insertAnswers(section: str):
    try:
        if section == "ThreatHunting":
            r = requests.get('https://docs.google.com/spreadsheets/d/1-fEFMqpci_dIA6SEvRs2YIQk28XJdnKSEcMWyXhO9Oc/export?format=csv&gid=820859871')
            data = r.content
            df = pd.read_csv(BytesIO(data))
            db_client.insertAnswersToDB(df,section)
        elif section == "VulnerabilityManagement":
            r = requests.get('https://docs.google.com/spreadsheets/d/1PkE3888iGT0JnZkkr6GuvKhN3zEhnwmUcNTYiCJhoto/export?format=csv&gid=2042618344',error_bad_lines=False)
            data = r.content
            df = pd.read_csv(BytesIO(data),error_bad_lines=False)
            db_client.insertAnswersToDB(df,section)
        else:
            df = pd.DataFrame()
            return {'status_code':200, "message":"Wrong option!"}
        
    except Exception as e:
        traceException(e)
        db_exceptions(e)

@app.patch('/update/answers',status_code=status.HTTP_200_OK,name="update-answers")
async def updateAnswers():
    try:
        db_client.updateAnswersToDB()
    except Exception as e:
        traceException(e)
        db_exceptions(e)

@app.get('/fetch/answers/{section}',status_code=status.HTTP_200_OK,name="fetch-answers")
async def fetchAnswers(section:str):
    try:
        res=db_client.fetchAnswersFromDB(section)
        return {"status_code":200,"message":res}
    except Exception as e:
        traceException(e)
        db_exceptions(e)

@app.get('/plot/graph/{section}/{x_axis}/{y_axis}/{kind}',status_code=status.HTTP_200_OK,name="plot-graph")
async def plotGraph(section: str,x_axis: str,y_axis: str, kind: str ):
    try:
        if section == "ThreatHunting":
            r = requests.get('https://docs.google.com/spreadsheets/d/1-fEFMqpci_dIA6SEvRs2YIQk28XJdnKSEcMWyXhO9Oc/export?format=csv&gid=820859871')
            data = r.content
            df = pd.read_csv(BytesIO(data))
            plotGraphUsingDF(df,x_axis,y_axis,kind)
        elif section == "VulnerabilityManagement":
            r = requests.get('https://docs.google.com/spreadsheets/d/1PkE3888iGT0JnZkkr6GuvKhN3zEhnwmUcNTYiCJhoto/export?format=csv&gid=2042618344',error_bad_lines=False)
            data = r.content
            df = pd.read_csv(BytesIO(data))
            plotGraphUsingDF(df,x_axis,y_axis,kind)
        else:
            df = pd.DataFrame()
    except Exception as e:
        traceException(e)
    return {"status_code":200, "message":"Graph plotted successfully"}