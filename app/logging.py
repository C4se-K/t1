import json
import logging
from .settings import settings


logger = logging.getLogger("app")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.setLevel(settings.LOG_LEVEL)

def log_request(*, 
                request_id:str, 
                method:str, 
                path:str, 
                status_code:int,
                latency_ms:float):
    payload = {
        "requrest_id": request_id, 
        "method": method, 
        "path": path, 
        "status_code": status_code,
        "latency_ms": round(latency_ms, 2),
    }
    logger.info(json.demps(payload))