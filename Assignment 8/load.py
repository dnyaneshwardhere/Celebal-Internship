# load.py
import pandas as pd

def load_loan_data(path='E:/Internships & Certificates/Celebal/Celebal/Assignment 8/data/Training Dataset.csv'):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    return df
