import pandas as pd
import numpy as np

# This code calculates statistical metrics for a dataset using pandas.
# It computes the range, quartiles, interquartile range, outlier bounds,
# variance, standard deviation, and provides a summary of the dataset.

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 78, 110]

arr = pd.Series(data)

print(f"Range: {arr.max() - arr.min()}")

print(f"Q1: {arr.quantile(1/4)}")
print(f"Q2: {arr.quantile(2/4)}")
print(f"Q3: {arr.quantile(3/4)}")
print(f"Q4: {arr.max()}")

inter_quantile = arr.quantile(3/4) - arr.quantile(1/4)
print(f"\nInter Quartile: {inter_quantile}")
lower_bound = arr.quantile(0.25) - (1.5 * inter_quantile)
print(f"Lower Bound (to outlier): {lower_bound}")
upper_bound = arr.quantile(0.75) + (1.5 * inter_quantile)
print(f"Upper Bound (to outlier): {upper_bound}") # IMPORTANT TO DETECT OUTLIERS

print(f"\nDeviation: {list((arr - arr.mean())**2)}")
print(f"Variance: {arr.var()}")
print(f"Standard Deviation: {arr.std()}")

print(f"\nSummary: \n{arr.describe()}")
