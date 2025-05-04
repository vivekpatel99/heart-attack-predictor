import os

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from uvicorn import run as app_run

from entity.config_entity import HeartAttackPredictorConfig
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import HeartAttackClaassifier, HeartAttackPredictor
from src.pipline.training_pipeline import TrainingPipeline

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to Heart Attack Prediction API"}


@app.post("/predict")
async def predict(input_data: HeartAttackPredictor):
    try:
        input_df = pd.DataFrame([input_data.model_dump()])
        predict_config = HeartAttackClaassifier(prediction_pipeline_config=HeartAttackPredictorConfig())
        result = predict_config.predict(input_df)[0]
        status = "Response-Yes" if result == 1 else "Response-No"
        return {"status": status}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=int(APP_PORT), reload=True)
