# FastAPI imports
from fastapi.exceptions import HTTPException
from fastapi import status
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from datetime import timedelta

# App imports
from database import Session, engine
from messages import ErrMessages, SucMessages
from models import User, Project


session = Session(bind=engine)


def validate_email(email: str):
    if session.query(User).filter(User.email == email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrMessages.Err_Email_Already_Exist,
        )


def validate_username(username: str):
    if session.query(User).filter(User.username == username).first():
        raise HTTPException(
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


def login_action(username: str, password: str):
    db_user = session.query(User).filter(User.username == username).first()
    if not db_user or not check_password_hash(db_user.password, password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username Or password",
        )
    time_limit = timedelta(days=1)
    access_token = AuthJWT().create_access_token(
        subject=db_user.username, expires_time=time_limit
    )
    refresh_token = AuthJWT().create_refresh_token(
        subject=db_user.username, expires_time=time_limit
    )

    access_token = access_token
    refresh_token = refresh_token
    response = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "id": db_user.id,
        "username": db_user.username,
    }
    return response


def create_project(
    user: str,
    title: str,
    description: str,
    project_url: str,
    image_url: str,
):
    new_project = Project(
        title=title,
        description=description,
        project_url=project_url,
        image_url=image_url,
    )
    user = session.query(User).filter(User.username == user).first()
    new_project.user = user
    session.add(new_project)
    session.commit()
    return new_project.__dict__


def update_project(project: Project):
    pass
