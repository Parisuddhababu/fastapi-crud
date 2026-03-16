from fastapi import APIRouter
from models.user_model import UserSignup, UserLogin
from services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])

service = UserService()

@router.post("/signup")
async def signup(user: UserSignup):
    return await service.signup(user)

@router.post("/login")
async def login(user: UserLogin):
    return await service.login(user)