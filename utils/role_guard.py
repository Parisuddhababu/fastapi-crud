from fastapi import Depends, HTTPException
from utils.auth_guard import verify_token

def require_admin(user=Depends(verify_token)):

    role = user.get("role")

    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user