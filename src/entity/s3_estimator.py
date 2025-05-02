import sys

from pandas import DataFrame

from src.cloud_storage.aws_storage import SimpleStorageService
from src.entity.estimator import MyModel
from src.exception import MyException


class Proj1Estimator:
    """
    This class is used to save and retrieve our model from s3 bucket and to do prediction
    """

    def __init__(
        self,
        bucket_name,
        model_path,
    ):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.model_path = model_path
        self.s3 = SimpleStorageService()
        self.loaded_model: MyModel = None

    def is_model_present(self, model_path: str) -> bool:
        """
        Checks if a specified S3 key path (file path) is available in the specified bucket.

        Args:
            model_path (str): Key path of the file to check.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        try:
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except MyException as e:
            print(e)
            return False

    def _load_model(self) -> MyModel:
        """
        Loads a serialized model from the specified S3 bucket.

        Returns:
            object: The deserialized model object.
        """
        try:
            return self.s3.load_model(model_name=self.model_path, bucket_name=self.bucket_name)
        except Exception as e:
            raise MyException(e, sys) from e

    def save_model(self, from_file, remove: bool = False) -> None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        try:
            self.s3.upload_file(from_file, to_filename=self.model_path, bucket_name=self.bucket_name, remove=remove)
        except Exception as e:
            raise MyException(e, sys)

    def predict(self, dataframe: DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self._load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise MyException(e, sys)
