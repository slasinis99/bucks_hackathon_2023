# -*- coding: utf-8 -*-
"""
@author: recon
"""
import numpy as np
from training_data import get_training_data
from network import Network
from fc_layer import FCLayer
from activation_layer import ActivationLayer
from activation_functions import tanh, tanh_prime
from error_functions import mse, mse_prime
    
#Test an XOR Network
# training data
x_train = np.array(get_training_data())
y_train = np.array([[[0.015625]],[[0.015625]],[[0.515625]]])

#Network
net = Network()
net.add(FCLayer(384, 256))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(256, 192))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(192, 128))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(128, 96))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(96, 64))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(64, 48))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(48, 32))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(32, 24))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(24, 16))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(16, 1))
net.add(ActivationLayer(tanh, tanh_prime))

#Train
net.use(mse, mse_prime)
net.fit(x_train,y_train, epochs=20000, learning_rate=0.1)

#Test
out = net.predict(x_train[0])
print(out)
out = net.predict(x_train[1])
print(out)
out = net.predict(x_train[2])
print(out)