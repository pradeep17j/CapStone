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
