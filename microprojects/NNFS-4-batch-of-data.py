#Neural networks are trained in batces of inputs
#Why?
# 1. Faster as inputs can be trained in parallel
# 2. (main reason) prevents overfitting as it can draw essentially a line of best fit
# 		between the input more generally instead of per datapoint

import numpy as np

inputs = [
	[1.0, 2.0, 3.0, 2.5],
	[2.0, 5.0, -1.0, 2.0],
	[-1.5, 2.7, 3.3, -0.8]]

weights = [
	[0.2, 0.8, -0.5, 1.0],
	[0.5, -0.91, 0.26, -0.5],
	[-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]

#we end up with two matrices, so we preform, matrix mulitplication!
#matrices in, matrix out
outputs = np.dot(inputs, np.array(weights).T) + biases
print(outputs)