from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

T = TypeVar('T')

class Login(BaseModel):
    username: str
    password: str

class Register(BaseModel):
    # id: str
    username: str
    password: str
    email: str
    phone_number: str
    first_name: str
    last_name: str

class ResponseSchema(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None

#token
class  TokenResponse(BaseModel):
    access_token: str
    token_type: str
    