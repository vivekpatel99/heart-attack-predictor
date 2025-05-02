import os

import boto3

from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, REGION_NAME


class S3Client:
    s3_client = None
    s3_resource = None

    def __init__(self, region_name: str | None = REGION_NAME):
        """
        This Class gets aws credentials from env_variable and creates an connection with s3 bucket
        and raise exception when environment variable is not set
        """
        if S3Client.s3_resource is None or S3Client.s3_client is None:
            __access_key_id = os.environ.get(AWS_ACCESS_KEY_ID_ENV_KEY)
            __secret_access_key = os.environ.get(AWS_SECRET_ACCESS_KEY_ENV_KEY)
            if __access_key_id is None:
                raise Exception(f"Environment variable {AWS_ACCESS_KEY_ID_ENV_KEY} is not set")
            if __secret_access_key is None:
                raise Exception(f"Environment variable {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set")

            S3Client.s3_resource = boto3.resource(
                "s3",
                region_name=region_name,
                aws_access_key_id=__access_key_id,
                aws_secret_access_key=__secret_access_key,
            )
            S3Client.s3_client = boto3.client(
                "s3",
                region_name=region_name,
                aws_access_key_id=__access_key_id,
                aws_secret_access_key=__secret_access_key,
            )

        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
