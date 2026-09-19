#NNFS-2
# 4 inputs, 3 output neurons

import numpy as np

inputs = [1.0, 0.2, 0.5, 0.3]

weights = [
    [0.2, 1.0, 0.1, 0.5],
    [0.8, 0.8, 0.8, 0.8],
    [0.1, 0.4, 0.2, 0.9],
]

biases = [0.5, 1, 0.3]


outputs = []
for n_weight, n_bias in zip(weights, biases): #each output neuron has its  own  set of  weights  and biases
    output = n_bias

    for  weight, n_input in zip(n_weight,  inputs):
        output +=weight*n_input

    outputs.append(output)
print(outputs)

print(np.dot(weights, inputs) + biases)


# O -
# O - O
# O - O
# O - O
