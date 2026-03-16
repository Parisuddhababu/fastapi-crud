from fastapi import APIRouter
from models.user_model import User
from services.user_service import UserService
from utils.auth_guard import verify_token
from fastapi import Depends

from utils.role_guard import require_admin

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(verify_token)]
)

service = UserService()

@router.get("/")
async def get_users():      
    return await service.get_users()

@router.post("/")
async def create_user(user: User):
    return await service.create_user(user)

@router.get("/{user_id}")
async def get_user(user_id: str):
    return await service.get_user(user_id)


@router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    return await service.update_user(user_id, user)


@router.delete("/{user_id}")
async def delete_user(user_id: str, admin=Depends(require_admin)):
    return await service.delete_user(user_id)