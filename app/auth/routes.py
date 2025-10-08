from fastapi import APIRouter, HTTPException
from app.users import crud
from app.users.schemas import UserCreate, UserOut
from app.auth.schemas import UserLogin, Token
from app.core.security import create_access_token

router = APIRouter()

# -------------------------
# Register a new user
# -------------------------
@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    existing = await crud.get_user_by_username(user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = await crud.create_user(user)

    return UserOut(
        id=str(new_user["_id"]),
        username=new_user["username"],
        email=new_user["email"]
    )

# -------------------------
# Login and get access token
# -------------------------
@router.post("/login", response_model=Token)
async def login(user: UserLogin):  # ✅ Use UserLogin
    db_user = await crud.authenticate_user(user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": db_user["username"]})
    return Token(access_token=token, token_type="bearer")
