import sys

import pandas as pd
from pydantic import BaseModel

from src.entity.config_entity import HeartAttackPredictorConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception import MyException
from src.logger import logging


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
