import yfinance as yf
import plotly.graph_objects as go
from scipy.signal import argrelextrema
import numpy as np

# https://raposa.trade/blog/higher-highs-lower-lows-and-calculating-price-trends-in-python/

ticker = 'NQ=F'

#df = yf.download(tickers=ticker, period='6mo', interval='1d')
df = yf.download(tickers = ticker, start='2022-01-04', end='2022-05-26')

df = df.reset_index()

max_idx = argrelextrema(df['Close'].values, np.greater, order=5)[0]
min_idx = argrelextrema(df['Close'].values, np.less, order=5)[0]


fig1 = go.Figure(data=[go.Candlestick(x=df['Date'],
                                      open=df['Open'],
                                      high=df['High'],
                                      low=df['Low'],
                                      close=df['Close'])])
Size = 10
Width = 1

fig1.add_trace(
    go.Scatter(
        mode='markers',
        x=df.iloc[max_idx]['Date'],
        y=df.iloc[max_idx]['High'],
        marker=dict(
            color='darkred',
            size=Size,
            line=dict(
                color='MediumPurple',
                width=Width
            )
        ),
        showlegend=False
    )
)

fig1.add_trace(
    go.Scatter(
        mode='markers',
        x=df.iloc[min_idx]['Date'],
        y=df.iloc[min_idx]['Low'],
        marker=dict(
            color='forestgreen',
            size=Size,
            line=dict(
                color='MediumPurple',
                width=Width
            )
        ),
        showlegend=False
    )
)

# fig1.show()

fig1.write_html( 'output_file_name.html',
                   auto_open=True )
