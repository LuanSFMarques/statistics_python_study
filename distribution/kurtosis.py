import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

# This code calculates and visualizes the kurtosis of a dataset.
# It computes kurtosis using both Pandas and Scipy, and plots the data distribution.

data = pd.Series([10, 15, 20, 25, 30, 100, 150, 200, 250, 300, 
                  305, 310, 315, 320, 325, 330, 335, 340, 350, 400])

kurt_pandas = data.kurt()
print(f"Kurtosis (Pandas): {kurt_pandas:.4f}")

kurt_scipy = kurtosis(data)  # By default, Scipy gives "excess kurtosis"
print(f"Kurtosis (Scipy): {kurt_scipy:.4f}")

sns.histplot(data, kde=True, bins=10)
plt.axvline(data.mean(), color='red', linestyle='dashed', label='Mean')
plt.legend()
plt.title("Data Distribution with Kurtosis")
plt.show()
