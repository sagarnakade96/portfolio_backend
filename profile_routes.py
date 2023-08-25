from fastapi import APIRouter

profile_router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)


@profile_router.get("/")
async def hello():
    return {"message": "profile_data"}
