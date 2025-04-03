import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoClient
from src.constants import DATABASE_NAME
from src.exception import MyException


class projectData:
    """
    This class provides methods to convert the mongodb records to the csv
    """

    def __init__(self):
        try:
            self.mongo_client = MongoClient(db_name=DATABASE_NAME)
        except MyException as e:
            raise MyException(e,sys)
        
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            print("the len of the data", len(df))

            if 'id' in df.columns.tolist():
                df =df.drop(columns=['id'], axis=1)
            df.replace({'na':np.nan}, inplace=True)
            return df
        
        except MyException as e:
            raise MyException(e, sys)