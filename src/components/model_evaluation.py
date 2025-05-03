import sys
from dataclasses import dataclass
from math import log
from typing import Optional

import pandas as pd
from sklearn.metrics import f1_score

from src.components.data_transformation import DataTransformation
from src.constants import SCHEMA_FILE_PATH, TARGET_COLUMN
from src.entity.artifact_entity import DataIngestionArtifact, ModelEvaluationArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelEvaluationConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import load_object, read_yaml_file


@dataclass
class EvaluateModelResponse:
    trained_model_f1_score: float
    best_model_f1_score: float
    is_model_accepted: bool
    difference: float


class ModelEvaluation(DataTransformation):
    def __init__(
        self,
        model_evaluation_config: ModelEvaluationConfig,
        data_ingestion_artifact: DataIngestionArtifact,
        model_trainer_artifact: ModelTrainerArtifact,
    ):
        try:
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e, sys)
        self.model_eval_config = model_evaluation_config
        self.data_ingestion_artifact = data_ingestion_artifact
        self.model_trainer_artifact = model_trainer_artifact

    def get_best_model(self) -> Optional[Proj1Estimator]:
        """
        Method Name :   get_best_model
        Description :   This function is used to get model from production stage.

        Output      :   Returns model object if available in s3 storage
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            bucket_name = self.model_eval_config.bucket_name
            model_path = self.model_eval_config.s3_model_key_path
            proj1_estimator = Proj1Estimator(bucket_name=bucket_name, model_path=model_path)

            if proj1_estimator.is_model_present(model_path=model_path):
                return proj1_estimator
            return None
        except Exception as e:
            raise MyException(e, sys)

    def evaluate_model(self) -> EvaluateModelResponse:
        """
        Method Name :   evaluate_model
        Description :   This function is used to evaluate trained model
                        with production model and choose best model

        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            x, y = test_df.drop(TARGET_COLUMN, axis=1), test_df[TARGET_COLUMN]
            logging.info("Splitting data into train and test set")
            y = self._map_result_column(col=y)

            logging.info("Trained model loaded/exists.")
            trained_model_f1_score = self.model_trainer_artifact.metric_artifact.f1_score
            logging.info(f"F1_Score for this model: {trained_model_f1_score}")

            best_model_f1_score = None
            best_model = self.get_best_model()
            if best_model:
                logging.info("Computing F1_Score for production model..")
                y_hat_best_model = best_model.predict(x)
                best_model_f1_score = f1_score(y, y_hat_best_model)
                logging.info(f"F1_Score-Production Model: {best_model_f1_score}, F1_Score-New Trained Model: {trained_model_f1_score}")

            tmp_best_model_score = 0 if best_model_f1_score is None else best_model_f1_score
            result = EvaluateModelResponse(
                trained_model_f1_score=trained_model_f1_score,
                best_model_f1_score=tmp_best_model_score,
                is_model_accepted=trained_model_f1_score > tmp_best_model_score,
                difference=trained_model_f1_score - tmp_best_model_score,
            )
            logging.info(f"Result: {result}")
            return result

        except Exception as e:
            raise MyException(e, sys)

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        """
        Method Name :   initiate_model_evaluation
        Description :   This function is used to initiate all steps of the model evaluation

        Output      :   Returns model evaluation artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            print("------------------------------------------------------------------------------------------------")
            logging.info("Initialized Model Evaluation Component.")
            evaluate_model_response = self.evaluate_model()
            s3_model_path = self.model_eval_config.s3_model_key_path

            model_evaluation_artifact = ModelEvaluationArtifact(
                is_model_accepted=evaluate_model_response.is_model_accepted,
                s3_model_path=s3_model_path,
                trained_model_path=self.model_trainer_artifact.trained_model_file_path,
                changed_accuracy=evaluate_model_response.difference,
            )

            logging.info(f"Model evaluation artifact: {model_evaluation_artifact}")
            return model_evaluation_artifact
        except Exception as e:
            raise MyException(e, sys) from e
