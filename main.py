from fastapi import FastAPI
from auth_routes import auth_router
from profile_routes import profile_router
import uvicorn

app = FastAPI()

app.include_router(auth_router)
app.include_router(profile_router)

# For debugging the breakpoints in vs code

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)