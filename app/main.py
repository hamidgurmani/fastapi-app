
from fastapi import FastAPI
from app.config import settings
from app.database import engine, check_db

app = FastAPI()

# 🔹 ADD THIS BLOCK
@app.on_event("startup")
def startup_event():
    check_db()

# Existing routes (UNCHANGED)
@app.get("/")
def root():
    return {"message": "FastAPI app is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

