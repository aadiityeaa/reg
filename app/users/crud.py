from app.db import db
from app.users.schemas import UserCreate
from app.core.security import hash_password, verify_password

async def get_user_by_username(username: str):
    return await db["users"].find_one({"username": username})

async def create_user(user: UserCreate):
    # Hash password (truncate to 72 bytes for bcrypt)
    hashed_pw = hash_password(user.password)
    
    # Insert user into database
    new_user = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_pw
    }
    result = await db["users"].insert_one(new_user)
    new_user["_id"] = str(result.inserted_id)
    return new_user

async def authenticate_user(username: str, password: str):
    user = await get_user_by_username(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user
