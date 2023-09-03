# Fast API imports
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT

# Python imports

# App imports
from database import Session, engine
from messages import ErrMessages, SucMessages
from models import User
from schema import ProjectModel
from actions import create_project, update_project


session = Session(bind=engine)

profile_router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)


@profile_router.get("/")
async def hello():
    return {"message": "profile_data"}


# List API
@profile_router.get("/templates")
async def templates(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="nahhh")
    user = Authorize.get_jwt_subject()
    current_user = session.query(User).filter(User.username == user).first()
    return {"message": current_user.project}


@profile_router.post("/templates")
async def templates(project: ProjectModel, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="nahhh")
    user = Authorize.get_jwt_subject()
    return create_project(
        user=user,
        title=project.title,
        description=project.description,
        project_url=project.project_url,
        image_url=project.image_url,
    )


@profile_router.put("/templates/{id}")
async def template(id: int, project: ProjectModel, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="nahhh")
    user = Authorize.get_jwt_subject()
    return update_project(user=User)
