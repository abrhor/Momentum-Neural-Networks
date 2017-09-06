#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:12:00 2017

@author: student
"""

import autograd.numpy as np
from autograd import grad

class Network(object): # assumes one output, one latent layer
    def __init__(self, x_dim, hidden_dim, n):
        self.i = x_dim
        self.i_h = hidden_dim
        self.n = n
        self.w1 = np.random.randn(self.i, self.i_h)
        self.w2 = np.random.randn(self.i_h, 1)
        
    def train(x_data, y_data, alpha), epoch:
        c_vec = np.array([])
        for i in range(epoch):
            for X, k in zip(x_data, y_data):
                x = X
                hid = sigmoid(x.dot(self.w1)) #1 x i dot i x i_h = 1 x i_h
                y = hid.dot(self.w2) # 1 x i_h dot i_h x 1 = 1 x 1
                c = (y-k)**2
                c_f = sigmoid(c)
                c_vec = np.append(c_vec, c_f)
                nabla_h = sigmoid_prime(c) * 2. * (y-k) * hid
                start_nabla = sigmoid_prime(c) * 2. * np.multiply(self.w2, sigmoid_prime(hid))
                nabla_first = np.array([])
                start
                    
            
    def sigmoid(x):
        return 1 / (1+np.exp(-x))
        
    def sigmoid_prime(x):
        return sigmoid(x)*(1-sigmoid(x))
    
    def logitweight
