# from src.logger import logging


# logging.debug("test debug")
# logging.info("test info")
# logging.warning("test warning")
# logging.error("test error")

# from src.exception import MyException
# import sys

# try:
#     raise MyException("Test error", sys)
# except MyException:
    

from src.pipline.training_pipeline import TrainingPipeLine


pipeline = TrainingPipeLine()

pipeline.run_pipeline()
