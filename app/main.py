from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from app.auth.routes import router as auth_router
from app.ml.routes import router as ml_router

app = FastAPI()

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(ml_router, prefix="/ml", tags=["ml"])

BASE_DIR = Path(__file__).parent

@app.get("/")
def root():
    return FileResponse(BASE_DIR / "login.html")

@app.get("/login")
def login_page():
    return FileResponse(BASE_DIR / "login.html")

@app.get("/register")
def register_page():
    return FileResponse(BASE_DIR / "register.html")

@app.get("/dashboard")
def dashboard_page():
    return FileResponse(BASE_DIR / "dashboard.html")
