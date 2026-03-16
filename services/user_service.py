from database.db import user_collection
from bson import ObjectId
from utils.security import hash_password, verify_password
from utils.jwt_handler import create_access_token,create_refresh_token  

class UserService:

# get users
    async def get_users(self):
        users = []
        async for user in user_collection.find():
            user["_id"] = str(user["_id"])
            users.append(user)
        return users
    
# create user
    async def create_user(self, user):
        result = await user_collection.insert_one(user.dict())
        return {"message": "User created", "id": str(result.inserted_id)}
    
# get user by id
    async def get_user(self, user_id: str):

        user = await user_collection.find_one(
            {"_id": ObjectId(user_id)}
        )

        if user:
            user["_id"] = str(user["_id"])
            return user

        return {"error": "User not found"}
    
# update user
    async def update_user(self, user_id: str, user):

        result = await user_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user.dict()}
        )

        if result.modified_count == 1:
            return {"message": "User updated !"}

        return {"error": "User not found"}
    
# delete user
    async def delete_user(self, user_id: str):

        result = await user_collection.delete_one(
            {"_id": ObjectId(user_id)}
        )

        if result.deleted_count == 1:
            return {"message": "User deleted"}

        return {"error": "User not found"}

# signup user
    async def signup(self, user):

        existing_user = await user_collection.find_one(
            {"email": user.email}
        )

        if existing_user:
            return {"error": "Email already registered"}

        hashed_password = hash_password(user.password)

        new_user = {
            "name": user.name,
            "email": user.email,
            "password": hashed_password,
            "role": user.role
        }

        await user_collection.insert_one(new_user)

        return {"message": "User created successfully"}
    
# login user
    async def login(self, user):

        db_user = await user_collection.find_one(
            {"email": user.email}
        )

        if not db_user:
            return {"error": "Invalid credentials"}

        if not verify_password(user.password, db_user["password"]):
            return {"error": "Invalid credentials"}

        payload = {
            "user_id": str(db_user["_id"]),
            "role": db_user["role"]
        }

        access_token = create_access_token(payload)

        refresh_token = create_refresh_token(payload)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }