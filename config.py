import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_for_dev")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#jwt secret key
SECRET_KEY="homelanderlikesuperman"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30