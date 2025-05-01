import logging
import os
import sys

import certifi
import pymongo

from src.constants import DATABASE_NAME, MONGODB_URL_KEY
from src.exception import MyException

# Load the certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()


class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the MongoDB database.

    Attributes:
    ----------
    client : MongoClient
        A shared MongoClient instance for the class.
    database : Database
        The specific database instance that MongoDBClient connects to.

    Methods:
    -------
    __init__(database_name: str) -> None
        Initializes the MongoDB connection using the given database name.
    """

    client = None  # Shared MongoClient instance across all MongoDBClient instances

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters:
        ----------
        database_name : str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.

        Raises:
        ------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """
        try:
            # Check if a MongoDB client connection was aalready established. if not, create a new one.
            if MongoDBClient.client is None:
                mongo_db_url = os.environ.get(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment variable {MONGODB_URL_KEY} is not set")

                # Establish a new MongoDB connections
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            # Use the shared MongoClient instance
            self.client = MongoDBClient.client
            db_name = os.environ.get(database_name)
            self.database = self.client[db_name]  # connect to specific database
            self.database_name = database_name
            logging.info(f"Connected to MongoDB database: {database_name}")
        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)
