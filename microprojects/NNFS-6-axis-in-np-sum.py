#NNFS - 6
#Just for me, I didn't understand axes
#Essentially np.sum() can add in rows, grids, cubes etc
#you can choose which specific row, column or section of the cube you want to add

import numpy as np 

layer_outputs = np.array([
	[4.8, 1.21, 2.385],
	[8.9, -1.81, 0.2],
	[1.41, 1.051, 0.026]
])

print('Sum without axis')
print(np.sum(layer_outputs))

print("This will be identical as default IS None")
print(np.sum(layer_outputs, axis=None))

print("Another way to think of it as a matrix is where matrix == axis 0, or columns")
print(np.sum(layer_outputs, axis=0))


print("We want matrix == axis 1, or rows")
print(np.sum(layer_outputs, axis=1))