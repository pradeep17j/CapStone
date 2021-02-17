import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings
warnings.filterwarnings('ignore')

spy = yf.Ticker("SPY")

spy.info

spy.history(period="max")

# The ability to access options, if needed
spy.option_chain()

data = yf.download("SPY", start="2020-01-01", end="2020-12-31")

# Convert data to numpy array
stocks = data.to_numpy()

# Read data from variable data
data.head()

# Relax the number of decimal places to consider
data = data.round(2)

# Determine the shape of the dataset
data.shape

# Check to see if we have any null values
data.isnull().sum()

# Check the data types of each column
data.dtypes

# Plot a simple chart
data['Adj Close'].plot(figsize=(15, 8))
plt.show()

# Show day to day percentage change
data['Day_Perc_Change'] = data['Adj Close'].pct_change()*100
data.head()

# Drop first column, as it is nan
data.dropna(axis=0, inplace=True)

# Plot daily return
data['Day_Perc_Change'].plot(figsize= (12, 6), fontsize=12)