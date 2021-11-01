from typing import Callable
from fastapi import FastAPI
from fastapi import Depends, FastAPI
from util.database.dao_postgres import CrudOperations
#creating instance of crudoperations class
db_client=CrudOperations()
def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        print("bootstraping scripts come here eg : connecting to database")
        # master_model=db_client.getModels()
        # master_state=db_client.getMasterState()
        # master_etl=db_client.getMasterETL()
        #insertCache('Models', str(master_model))
        #insertCache('State', str(master_state))
        #insertCache('ETL', str(master_etl))
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def stop_app() -> None:
        print("shutdown scripts come here  eg: closing-db-connections")
        #flushing cache memory during server shutdown
        #client = redis.Redis()
        #client.flushdb()
    return stop_app