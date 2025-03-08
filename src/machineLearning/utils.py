import pandas as pd
from machineLearning.logger import logging
import pickle
from machineLearning.exception import CustomException
import sys
import os

def read_csv_data(self):
    student_data = pd.read_csv("artifacts/raw.csv")

    return student_data


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e :
        raise CustomException(e,sys)
