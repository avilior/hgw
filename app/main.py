from fastapi import FastAPI
from starlette.status import *
import logging
import os
from pathlib import Path

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

@app.get("/api/conf", status_code=HTTP_200_OK)
def get_conf():
    LOG.info("get configuration")
    conf_path = Path("/etc/hgw/")
    p = conf_path.glob('**/*')
    files = [str(x) for x in p if x.is_file()]
    return F"{files}"


