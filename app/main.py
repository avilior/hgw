from fastapi import FastAPI
from starlette.status import *
import logging
import os

LOG = logging.getLogger(__name__ )
app = FastAPI()

@app.get("/", status_code=HTTP_200_OK)
def get_greeting():
    greeting = os.getenv('GREETING',"Hello World - 2020")
    return greeting

@app.get("/api/healthz/", status_code=HTTP_200_OK)
def get_healthz():
    LOG.info("healthz called")
    return "healthy"

@app.get("/api/readiness/", status_code=HTTP_200_OK)
def get_readiness():
    LOG.info("readiness called")
    return "ready"


