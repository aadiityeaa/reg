# Registration (FastAPI + MongoDB)


## Setup
1. Create a virtualenv and activate it
2. Install deps: `pip install -r requirements.txt`
3. Set environment variables (example):
- MONGO_URI (default: mongodb://localhost:27017)
- MONGO_DB (default: registration)
- SECRET_KEY (set to a strong secret)
- ACCESS_TOKEN_EXPIRE_MINUTES (optional)
4. Run: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`


Endpoints:
- `POST /auth/register` -> register user (JSON body)
- `POST /auth/login` -> login (form data username + password)
- `GET /auth/me` -> get current user (Authorization: Bearer <token>)
- `POST /ml/predict` -> placeholder protected ML endpoint