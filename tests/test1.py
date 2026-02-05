from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status":"OK"}

def test_metrics():
    r = client.get("/metrics")
    assert r.status_code == 200
    text = r.text
    assert "http_reqests_total" in text
