from sqlalchemy import Column, Integer, String, DateTime, Boolean
from config import Base
import datetime

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime)
