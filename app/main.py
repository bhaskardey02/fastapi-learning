from fastapi import FastAPI

from app.routers import fraud

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Fraud Analytics API"
    }


app.include_router(fraud.router)