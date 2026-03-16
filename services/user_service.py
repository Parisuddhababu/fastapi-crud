from database.db import user_collection
from bson import ObjectId

class UserService:

    async def get_users(self):
        users = []
        async for user in user_collection.find():
            user["_id"] = str(user["_id"])
            users.append(user)
        return users

    async def create_user(self, user):
        result = await user_collection.insert_one(user.dict())
        return {"message": "User created", "id": str(result.inserted_id)}
    
    async def get_user(self, user_id: str):

        user = await user_collection.find_one(
            {"_id": ObjectId(user_id)}
        )

        if user:
            user["_id"] = str(user["_id"])
            return user

        return {"error": "User not found"}
    
    async def update_user(self, user_id: str, user):

        result = await user_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user.dict()}
        )

        if result.modified_count == 1:
            return {"message": "User updated !"}

        return {"error": "User not found"}
    
    async def delete_user(self, user_id: str):

        result = await user_collection.delete_one(
            {"_id": ObjectId(user_id)}
        )

        if result.deleted_count == 1:
            return {"message": "User deleted"}

        return {"error": "User not found"}