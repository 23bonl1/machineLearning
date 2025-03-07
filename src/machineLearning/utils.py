import pandas as pd
from machineLearning.logger import logging

def read_csv_data(self):
    student_data = pd.read_csv("artifacts/raw.csv")

    return student_data