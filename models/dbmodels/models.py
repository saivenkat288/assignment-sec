from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../")
from util.database.database_connection import Base



class UserDetails(Base):
    __tablename__ = "user_details"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)