from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import Base, engine
import tables.users as user_table
import routes.users as user_routes

user_table.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # React default
    "http://localhost:8000",  # For development
    "http://localhost:5173",  # Vite default
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    # Production domains
    "https://jwellery-six.vercel.app",
    # Add your production domains here
    # "https://yourdomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
)

app.include_router(user_routes.router)