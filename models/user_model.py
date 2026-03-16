from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user" 


class UserLogin(BaseModel):
    email: EmailStr
    password: str