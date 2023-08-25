from database import engine, Base
from models import User, Project

Base.metadata.create_all(bind=engine)
