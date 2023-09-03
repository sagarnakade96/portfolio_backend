from pydantic import BaseModel
from typing import Optional


class ProjectModel(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str]
    project_url: str
    image_url: str
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "this is testing title",
                "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.",
                "project_url": "https://github.com/login",
                "image_url": "https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1789&q=80",
            }
        }


class RegisterModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]
    is_admin: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@gmail.com",
                "password": "Pass@123",
                "is_staff": False,
                "is_active": False,
                "is_admin": False,
            }
        }


class LoginModel(BaseModel):
    username: str
    password: str
