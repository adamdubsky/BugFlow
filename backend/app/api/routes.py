from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    return {"message": "BugFlow backend is live"}
