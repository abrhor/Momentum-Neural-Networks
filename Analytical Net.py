#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:12:00 2017

@author: student
"""

import autograd.numpy as np
from autograd import grad

class Network(object): # assumes three output, one latent layer
    def __init__(self, x_dim, hidden_dim, n):
        self.i = x_dim
        self.i_h = hidden_dim
        self.n = n
        self.w1 = np.random.randn(self.i, self.i_h)
        self.w2 = np.random.randn(self.i_h, 3)
        
    def forward(x_data):
        x = x_data
        hid = x.dot(self.w1) #1 x i dot i x i_h = 1 x i_h
        out = hid.dot(self.w2) # 1 x i_h dot i_h x 3 = 1 x 3
        
