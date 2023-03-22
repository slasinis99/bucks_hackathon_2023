# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:02:34 2023

@author: recon
"""
from layer import Layer

class ActivationLayer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime
        
    #Returns the activated input
    def forward_propogation(self, input_data):
        self.inp = input_data
        self.outp = self.activation(self.inp)
        return self.outp
    
    #Returns input_error=dE/dX for a given output_error=dE/dY
    #learning_rate is not used because there are no "learnable" parameters
    def backward_propogation(self, output_error, learning_rate):
        return self.activation_prime(self.inp) * output_error