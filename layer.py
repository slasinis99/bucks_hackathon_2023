# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:34:42 2023

@author: recon
"""

class Layer:
    def __init__(self):
        self.inp = None
        self.outp = None
    
    #Computes the output Y of a layer for a given input X
    def forward_propogation(self, inp):
        raise NotImplementedError
    
    #Computes dE/dX for a given dE/dY (and update parameters if any)
    def backward_propogation(self, outp_error, learning_rate):
        raise NotImplementedError