from fastapi import APIRouter

router = APIRouter()

@router.get("/demo")
def demo():
    return {"msg": "This will connect to your ML project soon"}
