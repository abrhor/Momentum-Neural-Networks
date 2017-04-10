#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:11:53 2017

@author: student
"""

# Numerical functions
import numpy as np
import pandas as pd
from scipy.stats.mstats import zscore

# Technical indicator functions and data
import talib
import quandl

# Learning packages
import theano as T
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import LSTM

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

bmy = DataGenerator("BMY")
x_data, y_data = bmy.generate_input_datasets(), bmy.generate_output_datasets()

x_training, x_testing = x_data[:8475], x_data[8475:]
y_training, y_testing = y_data[:8475], y_data[8475:]

primary = Sequential()
primary.add(LSTM(4,input_shape=(5,)))
primary.add(LSTM(4, activation='sigmoid'))
primary.add(Dense(1))

primary.compile(optimizer='rmsprop', 
                loss='binary_crossentropy', 
                metrics=['accuracy'])

primary.fit(x_training, y_training, batch_size=20, epochs=10, shuffle=False)
score, accuracy = primary.evaluate(x_testing, y_testing, batch_size=20, verbose=0)

print("Score: ", score)
print("Accuracy: ", accuracy)

primary.save('PrimaryLSTM.h5')








