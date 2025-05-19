from fastapi import APIRouter, Depends, HTTPException
from models.users import Login, Register, ResponseSchema, TokenResponse
from sqlalchemy.orm import Session
from config import get_db
from passlib.context import CryptContext
from repository.users import UsersRepo , JWTRepo
from tables.users import Users

router = APIRouter(
    tags={"Authentication"},
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/signup")
async def signup(request: Register, db: Session = Depends(get_db)):
    try:
        _user = Users(
        username = request.username,
        password = pwd_context.hash(request.password),
        email = request.email,
        phone_number = request.phone_number,
        first_name = request.first_name,
        last_name = request.last_name)
        UsersRepo.insert(db, _user)
        return ResponseSchema(
            code="200",
            status="success",
            message="User created successfully",
            result=_user
        ).dict(exclude_none=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
async def login(request: Login, db: Session = Depends(get_db)):
    try: 
        _user = UsersRepo.find_by_username(db, Users, request.username)
        if not pwd_context.verify(request.password, _user.password):
            return ResponseSchema(
                code="401",
                status="error",
                message="Invalid credentials",
                result=None
            ).dict(exclude_none=True)
        token = JWTRepo.generate_token({'sub': _user.username})
        return ResponseSchema(
            code="200",
            status="success",
            message="Login successful",
            result=TokenResponse(
                access_token=token,
                token_type="bearer"
            ).dict(exclude_none=True)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


        