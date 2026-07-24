from fastapi import APIRouter
import pandas as pd

from app.ml_model import model
from app.schemas import PredictionRequest

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post("/")
def predict(request: PredictionRequest):
    
    df = pd.DataFrame([request.model_dump()])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {"prediction": int(prediction),"fraud_probability": round(float(probability), 4)}