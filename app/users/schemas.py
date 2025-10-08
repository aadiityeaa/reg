from pydantic import BaseModel, EmailStr
from typing import Optional

# Base user model (common fields)
class UserBase(BaseModel):
    email: EmailStr
    username: str

# Model for user registration
class UserCreate(UserBase):
    password: str

# Model for returning user data (response)
class UserOut(UserBase):
    id: str  # MongoDB ObjectId is stringified in responses

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2
