import os
import pymongo
import sys
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY


ca = certifi.where()

class MongoClient:
    """ MongoClient for connecting to MongoDB """

    client = None

    def __init__(self, db_name: str = DATABASE_NAME) -> None:
        try:
            if MongoClient.client is None:
                mongo_url = os.getenv(MONGODB_URL_KEY)
                if mongo_url is None:
                    raise Exception(f"mongo url is not specified {MONGODB_URL_KEY}")
                
                MongoClient.client = pymongo.MongoClient(mongo_url, tlsCAFile = ca)

            self.client = MongoClient.client
            self.database = self.client[DATABASE_NAME]
            self.db_name = db_name

            logging.info("MongoDB connection successful.")
            
        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)
