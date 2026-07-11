from fastapi import FastAPI

from app.routers import fraud
from app.routers import auth

app = FastAPI()

app.include_router(fraud.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "Fraud Analytics API"}