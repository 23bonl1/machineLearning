from machineLearning.logger import logging
from machineLearning.exception import CustomException
from machineLearning.components.data_ingestion import DataIngestion
import sys

if __name__== "__main__":
    logging.info("execution started")

    try :
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom ecxeption")
        raise CustomException(e,sys)

