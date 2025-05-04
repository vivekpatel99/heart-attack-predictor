import sys

import pandas as pd
from pydantic import BaseModel, Field

from src.entity.config_entity import HeartAttackPredictorConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception import MyException
from src.logger import logging


class HeartAttackPredictor(BaseModel):
    age: int = Field(..., ge=14, le=120)
    gender: bool = Field(...)
    heart_rate: int = Field(..., ge=20, le=200)
    systolic_bp: int = Field(..., ge=30, le=250)
    diastolic_bp: int = Field(..., ge=30, le=250)
    blood_sugar: int = Field(..., ge=30, le=550)
    ck_mb: float = Field(..., ge=0, le=300)
    troponin: float = Field(..., ge=0, le=15)


class HeartAttackClaassifier(BaseModel):
    prediction_pipeline_config: HeartAttackPredictorConfig

    def predict(self, dataframe: pd.DataFrame) -> int:
        """
        This is the method of VehicleDataClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of VehicleDataClassifier class")
            model = Proj1Estimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result = model.predict(dataframe)

            return result

        except Exception as e:
            raise MyException(e, sys)
