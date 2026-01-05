from fastapi import fastAPI , APIRouter 

base_router = APIRouter()

@base_router.get("/")
def welcom():
    return{
        "message":"hello world"
    }
