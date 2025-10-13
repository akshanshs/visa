from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:

    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:

        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,
                                                           tls=True,
                                                           tlsCAFile=ca,
                                                           serverSelectionTimeoutMS=10000
                                                           )
            self.client = MongoDBClient.client
            self.database = self.client[DATABASE_NAME]
            self.database_name = database_name
            logging.info("Mongo DB Connection successful")
        except Exception as e:
            raise USvisaException(e, sys)

    def __getitem__(self, database_name: str):

        return self.client[database_name]