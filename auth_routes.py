# FastAPI imports
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT

# App imports
from schema import RegisterModel, LoginModel
from actions import (
    validate_email,
    validate_username,
    register_user,
    login_action,
)

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.get("/health")
async def health():
    # Authorize.jwt_required()
    return {"message": "healthy like thor"}


@auth_router.post("/register")
async def signup(user: RegisterModel, status_code=status.HTTP_200_OK):
    try:
        validate_email(email=user.email)
        validate_username(username=user.username)
        register_user(
            username=user.username,
            email=user.email,
            password=user.password,
            is_staff=user.is_staff,
            is_active=user.is_active,
            is_admin=user.is_admin,
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="something went wrong"
        )


@auth_router.post("/login")
async def login(user: LoginModel, Authorize: AuthJWT = Depends()):
    return login_action(username=user.username, password=user.password)
