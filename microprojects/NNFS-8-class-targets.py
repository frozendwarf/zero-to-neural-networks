#NNFS - 8
#Each list (vector) is a set if outputs with confidence scores
#here it could be dog cat or human
#confident and right = low loss
#confident and wrong = high los
#uncertain and right = medium los

import numpy as np

softmax_outputs = np.array([
	[0.7, 0.1, 0.2],
	[0.1, 0.5, 0.4],
	[0.02, 0.9, 0.08]
])
class_targets = [0,1,1]

for target_i, distribution in zip(class_targets, softmax_outputs):
	pass
	#print(distribution[target_i])

#alternatively:
#print(softmax_outputs[range(len(softmax_outputs)), class_targets])

#and now the negative log, 
print(-np.log(softmax_outputs[range(len(softmax_outputs)), class_targets]))