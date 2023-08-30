from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class TimeStampedBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now())


class User(TimeStampedBase):
    __tablename__ = "user"
    username = Column(String(25), unique=True)
    email = Column(String(25), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    project = relationship("Project", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"


class Project(TimeStampedBase):
    __tablename__ = "project"
    title = Column(String(25), nullable=True)
    description = Column(Text, nullable=True)
    project_url = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="project")

    def __repr__(self):
        return f"<Project {self.title}>"
