import pandas as pd
import numpy as np

# This code calculates Cyhelsky Skewness, a measure of asymmetry in a dataset.

def skewness(arr:pd.Series) -> float:
    below = arr[arr < arr.mean()]
    above = arr[arr > arr.mean()]
    
    return (len(below) - len(above)) / len(arr)

symmetric_data = pd.Series([11, 14, 17, 18, 27, 27, 29, 31, 38, 39])
print(skewness(symmetric_data))