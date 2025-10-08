from pydantic import BaseModel, EmailStr

# Base user model (common fields)
class UserBase(BaseModel):
    email: EmailStr
    username: str

# Model for registration
class UserCreate(UserBase):
    password: str

# Model for login
class UserLogin(BaseModel):
    username: str
    password: str

# Model for returning user data (response)
class UserOut(UserBase):
    id: str  # MongoDB ObjectId as string

    class Config:
        from_attributes = True  # for Pydantic v2

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
