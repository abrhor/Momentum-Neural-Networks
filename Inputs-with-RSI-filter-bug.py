#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:18:20 2017

@author: student
"""

import numpy as np
import pandas as pd
import talib
import theano as T
import quandl
from scipy.stats.mstats import zscore

quandl.ApiConfig.api_key = "zGTzKK6n5ryjuEJXxHxs"
  
class DataGenerator(object):
    def __init__(self, ticker):
        self.df = quandl.get("WIKI/" + ticker)
        self.close = np.array(self.df.loc[:, "Close"].tolist())
        self.highs = np.array(self.df.loc[:, "High"].tolist())
        self.lows = np.array(self.df.loc[:, "Low"].tolist())
        self.volume = np.array(self.df.loc[:, "Volume"].tolist())
        self.rsi = talib.RSI(self.close)[14:]
  
    def percent_change(self):
        pct = self.df.pct_change()
        close = pct.loc[:, "Close"].tolist()[1:]
        return close
  
    def create_factors(self):
        def factors():
            rsi = self.rsi
            upper, mid, lower = talib.BBANDS(self.close)
            bbwidth = (upper - lower) / mid
            mfi = talib.MFI(high=self.highs, low=self.lows, close=self.close, volume=self.volume, timeperiod=14)
            willr = talib.WILLR(self.highs, self.lows, self.close)
            roc = talib.ROC(self.close)
            return rsi, mfi[14:], bbwidth[14:], roc[14:], willr[14:]
        return factors()
    
    def z_scores(self):
        rsi, mfi, bbwidth, roc, willr = self.create_factors()
        rsi_z, mfi_z, bbwidth_z, roc_z, willr_z = zscore(rsi), zscore(mfi), zscore(bbwidth), zscore(roc), zscore(willr)
        return rsi_z, mfi_z, bbwidth_z, roc_z, willr_z
    
    def generate_input_datasets(self):
        rsi_z, mfi_z, bbwidth_z, roc_z, willr_z = self.z_scores()
        x_data = np.array(list(zip(rsi_z, mfi_z, bbwidth_z, roc_z, willr_z)))
        price = self.close[14:]
        return x_data
    
    def generate_output_datasets(self):
        y_data = np.array([])
        returns = self.percent_change()
        for i in returns[13:]:
            if i > 0.:
                y_data = np.append(y_data, 1.)
            else:
                y_data = np.append(y_data, 0.)
        return y_data
    
    
        
        
    


example = DataGenerator("TSLA")

x = example.generate_input_datasets()
y = example.generate_output_datasets()
rsi = example.rsi

x_prime = np.array([1., 2., 3., 4., 5.])
y_prime = np.array([])
for a, b, c in zip(x,y,rsi):
    if c > 66. or c < 34.:
        x_prime = np.vstack([x_prime, a])
        y_prime = np.append(y_prime, b)

x_prime = np.delete(x_prime, 0)
print(len(x_prime), len(y_prime))






        