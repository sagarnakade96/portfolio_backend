# FastAPI imports
from fastapi.exceptions import HTTPException
from fastapi import status
from werkzeug.security import generate_password_hash, check_password_hash

# App imports
from database import Session, engine
from messages import ErrMessages, SucMessages
from models import User

session = Session(bind=engine)


def validate_email(email: str):
    if session.query(User).filter(User.email == email).first():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrMessages.Err_Email_Already_Exist,
        )


def validate_username(username: str):
    if session.query(User).filter(User.username == username).first():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrMessages.Err_Username_Already_Exist,
        )


def register_user(
    username: str,
    email: str,
    password: str,
    is_staff: bool,
    is_active: bool,
    is_admin: bool,
):
    new_user = User(
        username=username,
        email=email,
        password=generate_password_hash(password),
        is_staff=is_staff,
        is_active=is_active,
        is_admin=is_admin,
    )

    session.add(new_user)
    session.commit()
    return new_user
