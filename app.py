from machineLearning.logger import logging
from machineLearning.exception import CustomException
from machineLearning.components.data_ingestion import DataIngestion
from machineLearning.components.data_transformation import DataTransformation, DataTransformationConfig
import sys

if __name__== "__main__":
    logging.info("execution started")

    try :
        #data_ingestion = DataIngestion()
        #data_ingestion.initiate_data_ingestion()
        #data_ingestion.initiate_data_ingestion()
        #data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation("artifacts/train_data.csv","artifacts/test_data.csv" )

    except Exception as e:
        logging.info("Custom ecxeption")
        raise CustomException(e,sys)

