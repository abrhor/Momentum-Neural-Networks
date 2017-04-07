#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:18:20 2017

@author: student
"""

import numpy as np
import talib as T
import quandl

def compute_z(data):
    def one_value(value, mean, std):
        numerator = value - mean
        denominator = std * 3.
        return numerator / denominator
    def total():
        output = np.array([])
        mean = np.nanmean(data)
        std = np.nanstd(data)
        for i in data:
            output = np.append(output, one_value(i, mean, std))
        return output
    return total()
  
class DataGenerator(object):
    def __init__(self, ticker):
        self.df = quandl.get("WIKI/" + ticker)
        self.close = np.array(self.df.loc[:, "Close"].tolist())
        self.highs = np.array(self.df.loc[:, "High"].tolist())
        self.lows = np.array(self.df.loc[:, "Low"].tolist())
        self.volume = np.array(self.df.loc[:, "Volume"].tolist())
  
    def percent_change(self):
        pct = self.df.pct_change()
        close = pct.loc[:, "Close"].tolist()[1:]
        return close
 # need multiple datasets at each time step. momentum, volume, etc. for different NNs
    def create_factors(self):
        def factors(): # Get rid of stochastics. Get other stuff
            rsi = T.RSI(self.close)
            upper, mid, lower = T.BBANDS(self.close)
            bbwidth = (upper - lower) / mid
            mfi = T.MFI(high=self.highs, low=self.lows, close=self.close, volume=self.volume, timeperiod=14)
            fastk, fastd = T.STOCHF(self.highs, self.lows, self.close)
            return rsi[14:], mfi[14:], bbwidth[4:], fastk[6:], fastd[6:]
        return factors()
    # Make all from [14:] Can't do anything with partial data
    
    def z_scores(self): # note you make an assumption in using a constant mean/std.
        factors = self.create_factors()
        rsi_z, mfi_z, bbwidth_z, fastk_z, fastd_z = compute_z(factors[0]), compute_z(factors[1]), compute_z(factors[2]), compute_z(factors[3]), compute_z(factors[4])
        return rsi_z, mfi_z, bbwidth_z, fastk_z, fastd_z
    
    def generate_datasets(self): # Dont do this. Just nto an array with an sub-array for each time step
        rsi_z, mfi_z, bbwidth_z, fastk_z, fastd_z = self.z_scores()
        datasets = {}
        N = len(self.close) - 14
        for i in range(N):
            datasets[i] = i
        for i in datasets:
            transport = rsi_z[-14-i:len(rsi_z)+1-i], mfi_z[-10-i:len(mfi_z)+1-i], bbwidth_z[-5-i:len(bbwidth_z)+1-i], fastk_z[-10-i:len(fastk_z)+1-i], fastd_z[-10-i:len(fastd_z)+1-i]
            actual = np.array([])
            for m in transport:
                for n in m:
                    actual = np.append(actual, n)
            datasets[i] = actual
        return datasets        
