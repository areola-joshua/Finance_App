#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#Simple Stock Price App

shown here are the stock prices and volume by Google!

""")

tickerSymbol = 'GOOGL'  #Ticker Symbol

tickerData = yf.Ticker(tickerSymbol) #get data on this ticker

#get historical prices for this ticker
tickerDf = tickerData.history(period='Id', start='2010-5-31', end='2015-5-31')
# --> Open   High   Low Close   Volume   Dividends   Stock Splits 

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

