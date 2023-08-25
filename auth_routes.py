# FastAPI imports
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

# App imports
from schema import RegisterModel
from actions import (
    validate_email,
    validate_username,
    register_user,
)

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.get("/health")
async def health():
    return {"message": "healthy like thor"}


@auth_router.post("/register")
async def signup(user: RegisterModel, status_code=status.HTTP_200_OK):
    try:
        validate_email(email=user.email)
        validate_username(username=user.username)
        register_user(username=user.username, email=user.email, password=user.password, is_staff=user.is_staff, is_active=user.is_active, is_admin=user.is_admin)

    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
