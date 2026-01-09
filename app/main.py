from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "FastAPI app is running",
        "environment": settings.ENVIRONMENT
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

