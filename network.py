# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:03:27 2023

@author: recon
"""


class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None
    
    #Add layer to the network
    def add(self, layer):
        self.layers.append(layer)
        
    #Set loss to use
    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime
    
    #predict output for a given input
    def predict(self, input_data):
        #Sample dimension first
        samples = len(input_data)
        result = []
        
        #run network over all samples
        for i in range(samples):
            #forward propogation
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propogation(output)
            result.append(output)
        
        return result
    
    #train the network
    def fit(self, x_train, y_train, epochs, learning_rate):
        #sample dimension first
        samples = len(x_train)
        
        #training loop
        for i in range(epochs):
            err = 0
            for j in range(samples):
                #forward propogation
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propogation(output)
                
                #Compute loss (for display purposes only)
                err += self.loss(y_train[j],output)
                
                #backward propogation
                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propogation(error, learning_rate)
                
            #Calculate average error on all samples
            err /= samples
            print(f"epoch {i+1}/{epochs}    error = {err}")