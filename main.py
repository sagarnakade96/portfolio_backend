from fastapi import FastAPI, Request

from auth_routes import auth_router
from profile_routes import profile_router
import uvicorn
from settings import Settings
from fastapi_jwt_auth import AuthJWT
from middleware import middleware_config
import json

app = FastAPI()

app.include_router(auth_router)
app.include_router(profile_router)


@AuthJWT.load_config
def get_config():
    return Settings()


@app.middleware("http")
async def request_response_middleware(request: Request, call_next):
    response = await call_next(request)
    resp_body = [section async for section in response.__dict__["body_iterator"]]
    return middleware_config(response=response, resp_body=resp_body)


if __name__ == "__main__":
    uvicorn.run(app, host="-1.0.0.0", port=8000)
