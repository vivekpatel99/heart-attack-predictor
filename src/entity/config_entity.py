import os
from dataclasses import dataclass
from datetime import datetime

import constants as CONST

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = CONST.PIPELINE_NAME
    artifact_dir: str = os.path.join(CONST.ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONST.DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, CONST.DATA_INGESTION_FEATURE_STORE_DIR, CONST.FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, CONST.DATA_INGESTION_INGESTED_DIR, CONST.TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, CONST.DATA_INGESTION_INGESTED_DIR, CONST.TEST_FILE_NAME)
    train_test_split_ratio: float = CONST.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = CONST.DATA_INGESTION_COLLECTION_NAME


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONST.DATA_VALIDATION_DIR_NAME)
    validation_report_file_path: str = os.path.join(data_validation_dir, CONST.DATA_VALIDATION_REPORT_FILE_NAME)


@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONST.DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(
        data_transformation_dir, CONST.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, CONST.TRAIN_FILE_NAME.replace("csv", "npy")
    )
    transformed_test_file_path: str = os.path.join(
        data_transformation_dir, CONST.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, CONST.TEST_FILE_NAME.replace("csv", "npy")
    )
    transformed_object_file_path: str = os.path.join(
        data_transformation_dir, CONST.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, CONST.PREPROCSSING_OBJECT_FILE_NAME
    )


@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONST.MODEL_TRAINER_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_dir, CONST.MODEL_TRAINER_TRAINED_MODEL_DIR, CONST.MODEL_FILE_NAME)
    expected_accuracy: float = CONST.MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path: str = CONST.MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    _n_estimators = CONST.MODEL_TRAINER_N_ESTIMATORS
    _min_samples_split = CONST.MODEL_TRAINER_MIN_SAMPLES_SPLIT
    _min_samples_leaf = CONST.MODEL_TRAINER_MIN_SAMPLES_LEAF
    _max_depth = CONST.MIN_SAMPLES_SPLIT_MAX_DEPTH
    _criterion = CONST.MIN_SAMPLES_SPLIT_CRITERION
    _random_state = CONST.MIN_SAMPLES_SPLIT_RANDOM_STATE


@dataclass
class ModelEvaluationConfig:
    changed_threshold_score: float = CONST.MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
    bucket_name: str = CONST.MODEL_BUCKET_NAME
    s3_model_key_path: str = CONST.MODEL_FILE_NAME


@dataclass
class ModelPusherConfig:
    bucket_name: str = CONST.MODEL_BUCKET_NAME
    s3_model_key_path: str = CONST.MODEL_FILE_NAME


@dataclass
class VehiclePredictorConfig:
    model_file_path: str = CONST.MODEL_FILE_NAME
    model_bucket_name: str = CONST.MODEL_BUCKET_NAME
