import numpy as np
import nnfs

nnfs.init()

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	def forward(self, input):
		pass

print(np.random.randn(6,6))