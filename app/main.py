from fastapi import FastAPI

from app.routers import fraud
from app.routers import auth
from app.routers import predict

app = FastAPI()

app.include_router(fraud.router)
app.include_router(auth.router)
app.include_router(predict.router)


@app.get("/")
def home():
    return {"message": "Fraud Analytics API"}