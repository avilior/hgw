from fastapi import FastAPI
from starlette.status import *

app = FastAPI()

@app.get("/", status_code=HTTP_200_OK)
def get_hello():
    return {"Hello":"World V2"}

@app.get("/api/healthy/", status_code=HTTP_200_OK)
def get_healthy():
    return "healthy"

@app.get("/api/ready/", status_code=HTTP_200_OK)
def get_ready():
    return "ready"


