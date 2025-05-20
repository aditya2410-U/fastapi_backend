from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import Base, engine
import tables.users as user_table
import routes.users as user_routes

user_table.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)