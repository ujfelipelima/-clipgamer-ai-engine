import os
import hmac
from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="ClipGamer AI Engine")

API_KEY = os.getenv("PROCESSING_SERVICE_API_KEY", "")

@app.get("/")
def home():
    return {
        "service": "ClipGamer AI",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/v1/jobs")
def create_job(authorization: str = Header(default="")):
    if not API_KEY:
        raise HTTPException(
            503,
            "API key not configured"
        )

    expected = f"Bearer {API_KEY}"

    if not hmac.compare_digest(authorization, expected):
        raise HTTPException(401, "Unauthorized")

    raise HTTPException(
        501,
        "Video processing engine is not implemented yet"
    )
  
