from fastapi import APIRouter
from models.user_model import User
from services.user_service import UserService

router = APIRouter()

service = UserService()

@router.get("/users")
async def get_users():
    return await service.get_users()

@router.post("/users")
async def create_user(user: User):
    return await service.create_user(user)

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    return await service.get_user(user_id)


@router.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    return await service.update_user(user_id, user)


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    return await service.delete_user(user_id)