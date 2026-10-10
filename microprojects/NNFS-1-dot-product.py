#The first concept of neural networks, each neuron's value is calculated via the dot product
#For each input going into the neuron, it is multiplied by it's weigt. 
#Finally the bias is added for the neuron

import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

outputs = np.dot(weights, inputs) + bias

print(outputs)
