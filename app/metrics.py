from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP reqests",
    ["route", "status_code"],
)

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "http_request_duration_seconds",
    "HTTP reqest duration in seconds",
    ["route"],
)

def record_http_request(*, 
                        route:str,
                        status_code:int,
                        duration_seconds:float):
    HTTP_REQUESTS_TOTAL.labels(route=route, status_code = str(status_code)).inc()
    HTTP_REQUEST_DURATION_SECONDS.labels(route=route).observe(duration_seconds)

def metrics_text() -> str:
    return generate_latest().decode("utf-8")
