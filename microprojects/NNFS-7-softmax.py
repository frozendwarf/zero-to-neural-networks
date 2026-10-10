#NNFS - 7
#from the book, showing softmax using raw python
#The idea is it gets all the raw outputs and put them between 0 and 1
#The value depends on how large or small the number is to the others
#e.g. numbers 0.5, 6.4, 1.3 -> 0.004, 0.99, 0.006
#or 1,1,1 -> 0.33, 0.33, 0.33

layer_outputs = [4.8, 1.21, 2.385]

E = 2.71828182846

exp_values = []
for output in layer_outputs:
	exp_values.append(E**output)
norm_base = sum(exp_values)
norm_values = []
for value in exp_values:
	norm_values.append(value/norm_base)
print(norm_values)


#also from the book, but now using numpy
import numpy as np 

layer_outputs = [4, 4, 4]

exp_values = np.exp(layer_outputs)
norm_values = exp_values / np.sum(exp_values)
print(norm_values)