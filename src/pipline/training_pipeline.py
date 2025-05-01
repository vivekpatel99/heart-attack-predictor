import logging
import sys

from src.components.data_ingestion import DataIngestion
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
    ModelTrainerConfig,
)
from src.exception import MyException

# from src.components.data_validation import DataValidation


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_evaluation_config = ModelEvaluationConfig()
        self.model_pusher_config = ModelPusherConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered start_data_ingestion method of TrainingPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from mongodb")
            logging.info("Exited start_data_ingestion method of TrainingPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys)

    # def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataIngestionArtifact:
    #     """
    #     This method of TrainPipeline class is responsible for starting data validation component
    #     """
    #     logging.info("Entered start_data_validation method of TrainingPipeline class")
    #     try:
    #         dataa_validation = DataValidation(
    #             data_validation_config=self.data_validation_config,
    #             data_ingestion_artifact=self.data_ingestion_artifact,
    #         )
    #     except Exception as e:
    #         raise MyException(e, sys)

    def run_pipeline(self) -> None:
        """
        This method of TrainPipeline class is responsible for running the pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            print(data_ingestion_artifact)
        except Exception as e:
            raise MyException(e, sys)
