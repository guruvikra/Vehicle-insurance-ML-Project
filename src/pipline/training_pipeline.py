import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact


class TrainingPipeLine:
    def __init__(self):
        self.data_ingestion_config =  DataIngestionConfig()

    try:
        def start_data_ingestion(self) -> DataIngestionArtifact:
            logging.info("started training pipeline")
            data_ingestions = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestions.initiate_data_ingestion()
            logging.info("finished data ingestion training pipeline")
            return data_ingestion_artifact

    except Exception as e:
        raise MyException(f"Error occurred in training pipeline: {e}", sys)        
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            # Run other pipeline steps here
            # ...

        except Exception as e:
            raise MyException(f"Error occurred during pipeline execution: {e}", sys)
