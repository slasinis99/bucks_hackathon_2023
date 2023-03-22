# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:46:43 2023

@author: recon
"""
import numpy as np

#Activation function and its derivative
def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1-np.tanh(x)**2