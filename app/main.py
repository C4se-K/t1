from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse, JSONResponse
import time
import uuid

from .settings import settings


app = FastAPI(title=settings.APP_NAME)

@app.get("/health")
def health():
    return {"status":"OK"}

@app.get("/metrics")
def metrics():
    return PlainTextResponse()