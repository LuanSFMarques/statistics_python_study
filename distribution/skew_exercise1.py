import pandas as pd
import matplotlib.pyplot as plt

# This code calculates the skewness of a sales dataset and visualizes its distribution.
# It prints the skewness value and plots a histogram of the sales data.

sales = pd.Series([150, 160, 165, 170, 200, 250, 300, 305, 310, 315, 
                   320, 330, 340, 350, 355, 360, 370, 375, 380, 385,
                   400, 420, 430, 450, 470, 500, 520, 530, 550, 600])

print(sales.skew())

plt.hist(sales)
plt.show()