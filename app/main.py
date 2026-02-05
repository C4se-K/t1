from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse, JSONResponse
import time
import uuid

from .settings import settings
from .logging import log_request
from .metrics import (record_http_request, metrics_text)


app = FastAPI(title=settings.APP_NAME)

@app.middleware("http")
async def overvability_middleware(request : Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.perf_counter()

    try:
        response: Response = await call_next(request)
    except:
        response = JSONResponse(status_code=500, content={"detail":"internal error"})\
        
    elapsed = time.perf_counter() - start
    latency_ms = elapsed * 1000.0

    response.headers["X-Request-Id"] = request_id

    route = request.url.path
    record_http_request(route=route, status_code = response.status_code, duration_seconds = elapsed)
    log_request(
        request_id=request_id,
        method=request.method,
        path = request.url.path,
        status_code=response.status_code,
        latency_ms=latency_ms,
    )

    return response

@app.get("/health")
def health():
    return {"status":"OK"}

@app.get("/metrics")
def metrics():
    return PlainTextResponse()