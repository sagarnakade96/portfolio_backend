# Fast API imports
from pydantic import BaseModel

# App imports


class Settings(BaseModel):
    authjwt_secret_key: str = (
        "67fb4e44e6617842123f1a66f64a3ebf580d051e1a6c09c389054a354f5e348b"
    )
