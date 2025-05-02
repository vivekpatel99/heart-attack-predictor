import sys

import numpy as np
import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder, StandardScaler

from src.constants import CURRENT_YEAR, SCHEMA_FILE_PATH, TARGET_COLUMN
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact
from src.entity.config_entity import DataTransformationConfig
from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import read_yaml_file, save_numpy_array_data, save_object


class DataTransformation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_transformation_config: DataTransformationConfig,
        data_validation_artifact: DataValidationArtifact,
    ):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_transformation_config = data_transformation_config
        self.data_validation_artifact = data_validation_artifact
        try:
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e, sys)

    # @staticmethod
    # def cols_preprocessor(source_df: pd.DataFrame, drop_cols: list):
    #     bp_split = source_df["Blood Pressure"].str.split("/", expand=True).astype(int)
    #     bp_split.columns = ["Systolic", "Diastolic"]
    #     source_df.drop(drop_cols, axis=1, inplace=True)
    #     source_df = pd.concat([source_df, bp_split], axis=1)
    #     return source_df

    def get_data_transformer_object(self) -> Pipeline:
        """
        Creates and returns a data transformer object for the data,
        including gender mapping, dummy variable creation, column renaming,
        feature scaling, and type adjustments.
        """
        logging.info("Entered get_data_transformer_object method of DataTransformation class")

        try:
            logging.info("Transformers Initialized: StandardScaler-MinMaxScaler")
            # Load schema configurations
            categorical_cols = self._schema_config["categorical_columns"]
            continuous_cols = self._schema_config["mm_columns"]
            logging.info("Cols loaded from schema.")
            categorical_xformer = OrdinalEncoder()
            continues_xformer = MinMaxScaler()

            preprocessor = ColumnTransformer(
                transformers=[("cat", categorical_xformer, categorical_cols), ("cont", continues_xformer, continuous_cols)],
                remainder="passthrough",  # Leaves other columns as they are
            )
            # Wrapping everything in a single pipeline
            final_pipeline = Pipeline(steps=[("Preprocessor", preprocessor)])
            logging.info("Final Pipeline Ready!!")
            logging.info("Exited get_data_transformer_object method of DataTransformation class")
            return final_pipeline
        except Exception as e:
            logging.exception("Exception occurred in get_data_transformer_object method of DataTransformation class")
            raise MyException(e, sys) from e

    def _map_gender_column(self, df) -> pd.DataFrame:
        """Map Gender column to 0 for Female and 1 for Male."""
        logging.info("Mapping 'Gender' column to binary values")
        df.Sex = df.Sex.map({"Female": 0, "Male": 1}).astype(int)
        return df

    def _drop_unwanted_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Drop unnecessary columns."""
        logging.info("Dropping unwanted columns")
        drop_col = self._schema_config["drop_columns"]
        df.drop(drop_col, axis=1, inplace=True)
        return df

    def _handle_blood_pressure_column(self, df) -> pd.DataFrame:
        """Split 'Blood Pressure' column into 'Systolic' and 'Diastolic' columns."""
        bp_split = df["Blood Pressure"].str.split("/", expand=True).astype(int)
        bp_split.columns = ["Systolic", "Diastolic"]

        df = pd.concat([df, bp_split], axis=1)
        return df

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        """
        Initiates the data transformation component for the pipeline.
        """
        try:
            logging.info("Data Transformation Started !!!")
            if not self.data_validation_artifact.validation_status:
                raise Exception(self.data_validation_artifact.message)

            # Load train and test data
            train_df = self.read_data(file_path=self.data_ingestion_artifact.trained_file_path)
            test_df = self.read_data(file_path=self.data_ingestion_artifact.test_file_path)
            logging.info("Train-Test data loaded")

            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            logging.info("Input and Target cols defined for both train and test df.")

            # Preprocessing
            input_feature_train_df = self._map_gender_column(df=input_feature_train_df)
            input_feature_train_df = self._handle_blood_pressure_column(df=input_feature_train_df)
            input_feature_train_df = self._drop_unwanted_columns(df=input_feature_train_df)

            input_feature_test_df = self._map_gender_column(df=input_feature_test_df)
            input_feature_test_df = self._handle_blood_pressure_column(df=input_feature_test_df)
            input_feature_test_df = self._drop_unwanted_columns(df=input_feature_test_df)
            logging.info("Custom transformations applied to train and test data")

            logging.info("Starting data transformation")
            preprocessor = self.get_data_transformer_object()
            logging.info("Got the preprocessor object")

            logging.info("Initializing transformation for Training-data")
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            logging.info("Initializing transformation for Testing-data")
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)
            logging.info("Transformation done end to end to train-test df.")

            logging.info("Applying SMOTEENN for handling imbalanced dataset.")
            smt = SMOTEENN(sampling_strategy="minority")
            input_feature_train_final, target_feature_train_final = smt.fit_resample(input_feature_train_arr, target_feature_train_df)
            input_feature_test_final, target_feature_test_final = smt.fit_resample(input_feature_test_arr, target_feature_test_df)
            logging.info("SMOTEENN applied to train-test df.")

            train_arr = np.c_[input_feature_train_final, np.array(target_feature_train_final)]
            test_arr = np.c_[input_feature_test_final, np.array(target_feature_test_final)]
            logging.info("feature-target concatenation done for train-test df.")

            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr)
            logging.info("Saving transformation object and transformed files.")

            logging.info("Data transformation completed successfully")
            return DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )

        except Exception as e:
            raise MyException(e, sys) from e
