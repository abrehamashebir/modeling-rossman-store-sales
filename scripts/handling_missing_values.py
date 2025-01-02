
import pandas as pd
import numpy as np

def fill_missing_mode(df):
    
    for obj_col in df.select_dtypes(include=['object']).columns:
        mode_values = df[obj_col].mode()[0]
        
        df[obj_col].fillna(mode_values, inplace = True)

    return df


def fill_missing_mean(df):

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)
    
    return df