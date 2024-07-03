import pandas as pd

def preprocess_data(df):
    # Select relevant features and handle missing values
    selected_features = ['Rating', 'Spec_score', 'RAM', 'Battery', 'Display', 'Camera', 'Price']
    df = df[selected_features].dropna()
    return df