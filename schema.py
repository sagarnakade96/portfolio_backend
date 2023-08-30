from pydantic import BaseModel
from typing import Optional


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
