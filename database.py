from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "postgresql://postgres:123456@localhost/fastdb",
    echo=True,
)

Base = declarative_base()
Session = sessionmaker()
