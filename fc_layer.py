# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:01:38 2023

@author: recon
"""
from layer import Layer
import numpy as np

#Inherit from base class Layer
class FCLayer(Layer):
    #input_size = number of input neurons
    #output_size = number of output neurons
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size,output_size) - 0.5
        self.bias = np.random.rand(1,output_size) - 0.5
    
    #Returns output for a given input
    def forward_propogation(self, input_data):
        self.inp = input_data
        self.outp = np.dot(self.inp, self.weights) + self.bias
        return self.outp
    
    #Computes dE/dW, dE/dB for a given output_error=dE/dY, Returns input_error=dE/dX
    def backward_propogation(self, output_error, learning_rate):
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.inp.T, output_error)
        #dBias = output_error
        
        #Update parameters
        self.weights -= learning_rate * weights_error
        self.bias -= learning_rate * output_error
        return input_error