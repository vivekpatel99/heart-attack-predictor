""" """

import os
from datetime import date

from matplotlib.dates import MO

# For MongoDB connection
DATABASE_NAME = "DB_NAME"
COLLECTION_NAME = "COLLECTION_NAME"
MONGODB_URL_KEY = "DB_CONNECTION_URL"

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.joblib"

TARGET_COLUMN = "Result"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.joblib"

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# --- AWS S3 related constant start with AWS VAR NAME
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"  # nosec B105
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"  # nosec B105
REGION_NAME: str | None = os.environ.get("REGION_NAME")


# --- Data Ingestion related constant start with DATA_INGESTION VAR NAME
DATA_INGESTION_COLLECTION_NAME: str | None = os.environ.get(COLLECTION_NAME)  # "Proj1-Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

# --- Data Validation related constant start with DATA_VALIDATION VAR NAME

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# --- Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# --- MODEL TRAINER related constant start with MODEL_TRAINER var name
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.joblib"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 750
MODEL_TRAINER_LEARNING_RATE = 0.007659266705050152
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101
MODEL_TRAINER_SUBSAMPLE = 0.8638068341586023
MODEL_TRAINER_SCALE_POS_WEIGHT = 3.0839016606865917


# --- MODEL Evaluation related constants
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "heart-attack-predictor"
MODEL_PUSHER_S3_KEY = "model-registry"


APP_HOST = os.environ.get("APP_HOST")
APP_PORT = os.environ.get("APP_PORT")


# {
#     "classifier": "XGBoost",
#     "n_estimators": 750,
#     "max_depth": 24,
#     "learning_rate": 0.007659266705050152,
#     "subsample": ,
#     "scale_pos_weight": 3.0839016606865917,
# }
