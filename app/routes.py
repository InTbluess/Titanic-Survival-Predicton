import pandas as pd

from fastapi import APIRouter

from app.model import pipeline
from app.schemas import (
    Passenger,
    PredictionResponse
)

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Titanic Survival Prediction API"
    }

@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(passenger: Passenger):

    df = pd.DataFrame([
        passenger.model_dump()
    ])

    prediction = pipeline.predict(df)

    probability = pipeline.predict_proba(df)

    return PredictionResponse(
        prediction=int(prediction[0]),
        survived_probability=float(probability[0][1]),
        died_probability=float(probability[0][0])
    )