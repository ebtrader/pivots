from scipy.signal import argrelextrema

# https://raposa.trade/blog/higher-highs-lower-lows-and-calculating-price-trends-in-python/

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

ticker = 'NQ=F'
yfObj = yf.Ticker(ticker)
data = yfObj.history(start='2020-01-01', end='2022-05-26')

max_idx = argrelextrema(data['Close'].values, np.greater, order=5)[0]
min_idx = argrelextrema(data['Close'].values, np.less, order=5)[0]

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

plt.figure(figsize=(15, 8))
plt.plot(data['Close'], zorder=0)
plt.scatter(data.iloc[max_idx].index, data.iloc[max_idx]['Close'],
  label='Maxima', s=100, color=colors[1], marker='^')
plt.scatter(data.iloc[min_idx].index, data.iloc[min_idx]['Close'],
  label='Minima', s=100, color=colors[2], marker='v')

plt.legend()
plt.show()
