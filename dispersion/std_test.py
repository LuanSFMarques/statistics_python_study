import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This code calculates and compares statistical metrics (standard deviation, mean, median, and outlier bound) for multiple datasets.

data1 = pd.Series([1,1,1,1,1,1,1])
data2 = pd.Series([1,1,1,1,1,2,3])
data3 = pd.Series([3,2,1,1,1,1,1])
data4 = pd.Series([1,1,1,1,1,2,10])

print(data1.std())
print(data2.std())
print(data3.std())
print(data4.std())
print()
print(data1.mean())
print(data2.mean())
print(data3.mean())
print(data4.mean())
print()
print(data1.median())
print(data2.median())
print(data3.median())
print(data4.median())

print(data4.quantile(0.75) + (1.5 * (data4.quantile(0.75) - data4.quantile(0.25))) )
