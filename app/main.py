from fastapi import FastAPI
from starlette.status import *

app = FastAPI()

@app.get("/", status_code=HTTP_200_OK)
def get_hello():
    return {"Hello":"World V2"}

@app.get("/api/healthz/", status_code=HTTP_200_OK)
def get_healthz():
    return "healthy"

@app.get("/api/readiness/", status_code=HTTP_200_OK)
def get_readiness():
    return "ready"


