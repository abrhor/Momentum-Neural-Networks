#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:18:20 2017

@author: student
"""

import numpy as np
import pandas as pd
import talib as T
import quandl

def compute_z(data):
  def one_value(value, mean, std):
    numerator = value - mean
    denominator = std * 3.
    return numerator / denominator
  def total(data):
    output = []
    mean = np.nanmean(data)
    std = np.nanstd(data)
    for i in data:
      output.append(one_value(i, mean, std))
    output = np.array(output)
    return output
  
class Classifier(self):
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
  
  def create_factors(self):
    def factors(self):
      rsi = T.RSI(self.close)[14:]
      upper, mid, lower = T.BBANDS(self.close)
      bbands = np.array([self.upper, self.mid, self.lower])
      bbwidth = (self.upper - self.lower) / self.mid
      mfi = T.MFI(high=self.highs, low=self.lows, close=self.close, volume=self.volume, timeperiod=14)
      fastk, fastd = STOCHF(self.highs, self.lows, self.close)
      faststo = np.array([fastk, fastd])
      return rsi, mfi, bbwidth, faststo, bbands
    
    def standards(self):
      factors = list(self.factors())
      zscores = np.array([])
      for i in factors[:3]:
        np.append(zscores, compute_z(factors))
      np.append(zscores, compute_z(factors[3][2])
      return zscores
    
    return self.standards()
 