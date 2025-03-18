import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew

# This code generates and visualizes datasets with different skewness levels.
# It creates symmetric, positively skewed, and negatively skewed distributions,
# calculates their skewness, and plots their histograms with KDE curves.

np.random.seed(42)
symmetric_data = np.random.normal(50, 10, 1000)  # Symmetric (Normal)
positive_skew_data = np.random.exponential(5, 1000)  # Positively Skewed
negative_skew_data = np.random.normal(50, 10, 1000) ** 2  # Negatively Skewed

df = pd.DataFrame({
    'Symmetric': symmetric_data,
    'Positive Skew': positive_skew_data,
    'Negative Skew': negative_skew_data
})

print("Skewness:")
print(df.skew())

plt.figure(figsize=(12, 4))

for i, column in enumerate(df.columns):
    plt.subplot(1, 3, i+1)
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"{column}\nSkewness: {df[column].skew():.2f}")

plt.tight_layout()
plt.show()
