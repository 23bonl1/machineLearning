import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from machineLearning.logger import logging
from machineLearning.exception import CustomException
from dataclasses import dataclass
from machineLearning.utils import read_csv_data
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train_data.csv')
    test_data_path:str=os.path.join('artifacts','test_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion sterted")
            student_data = read_csv_data(self)
            print(student_data.head(5))
            train_set, test_set = train_test_split(student_data,test_size=0.2,random_state=41)
            dataFrame = pd.DataFrame()
            dataFrame.to_csv(self.ingestion_config.test_data_path,index=False, header=True)
            dataFrame.to_csv(self.ingestion_config.train_data_path,index=False, header=True)

            logging.info("Data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

