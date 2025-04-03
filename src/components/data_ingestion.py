import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.logger import logging
from src.exception import  MyException
from src.data_access.proj1_data import projectData


class DataIngestion:

    def __init__(self, data_ingestion_config = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except MyException as e:
            raise MyException(e, sys)
        
    def export_data (self) -> pd.DataFrame:
        try:
            data = projectData() # this get the data from the collection
            logging.info("data is imported from the mongodb collection")
            df = data.export_collection_as_dataframe(collection_name = self.data_ingestion_config.collection_name)
            logging.info("data converetd to dataframe")
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            dir_path= os.path.dirname(feature_store_path)
            os.makedirs(dir_path, exist_ok=True)
            df.to_csv(feature_store_path, index=False, header=True)
            logging.debug("done")

            return df

        except MyException as e:
            raise MyException(e, sys)
        
    def split_data_into_train_test(self, dataframe: pd.DataFrame) -> None:
        """
        Methofs Name: train_test_split from model selection
        it split the data into train and test
        """

        try:
            train_set,test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("data split into train and test")
            logging.info(len(train_set))
            dir_path  = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok = True)
            logging.info("training folder created")

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info("train and test data exported to files")

        except Exception as e:
            raise MyException(e, sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            df = self.export_data()

            logging.info("got the data from mongodb")

            self.split_data_into_train_test(df)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, test_file_path= self.data_ingestion_config.testing_file_path)

            return data_ingestion_artifact
        
        except MyException as e:
            raise MyException(e, sys)
