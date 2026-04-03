from fastapi import FastAPI, Request, HTTPException
from .rate_limiter import check_rate_limit
import time

app = FastAPI(title="DDoS Defense Lab")

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host

    if not check_rate_limit(ip):
        raise HTTPException(status_code=429, detail="Too many requests")

    response = await call_next(request)
    return response

@app.get("/")
def home():
    return {"message": "API Online"}

@app.get("/api")
def api():
    time.sleep(0.05)  # simula processamento
    return {"status": "ok"}

@app.get("/login")
def login():
    time.sleep(0.1)
    return {"login": "success"}