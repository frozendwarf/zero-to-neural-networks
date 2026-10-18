#This is my attempt of making a neural network from complete scratch, no libraries

#The following training data I got chatGPT to generate for me, the idea is I am predicting server failure:
# Training data for a server failure classification neural network.
# Each input contains:
#   [server_temperature, CPU_usage]
#   Temperature is measured in degrees Celsius.
#   CPU usage is a percentage from 0 to 100.
#
# Each corresponding output is the correct classification:
#   0 = Normal operation
#   1 = Server under heavy load
#   2 = High risk of server failure
#
# These are illustrative training examples, not real failure predictions.
# The network will learn patterns linking server conditions to classifications.

X = [
    [35, 20],
    [40, 30],
    [32, 15],
    [45, 40],
    [50, 85],
    [55, 90],
    [48, 95],
    [60, 80],
    [75, 95],
    [85, 90],
    [90, 98],
    [80, 100],
]

y = [
    0,  # Normal operation
    0,  # Normal operation
    0,  # Normal operation
    0,  # Normal operation
    1,  # Heavy load
    1,  # Heavy load
    1,  # Heavy load
    1,  # Heavy load
    2,  # High failure risk
    2,  # High failure risk
    2,  # High failure risk
    2,  # High failure risk
]

E = 2.71828182845904523536028747135266249775724709369995

#-------------------------
#--------FUNCTIONS--------
#-------------------------
def dotProduct(list1, list2):
	output = 0
	for i in range(len(list1)):
		output += list1[i] * list2[i]
	return output

def addBiases(matrix, biases):
    return [[v + b for v, b in zip(vector, biases)] for vector in matrix]

def clip(values, minimum, maximum):
    return [max(minimum, min(v, maximum)) for v in values]


def transpose(array):
	rows = len(array)
	columns = len(array[0])
	transposed = [[None] * rows for _ in range(columns)]

	for i, row in enumerate(array):
		for j, value in enumerate(row):
			transposed[j][i] = array[i][j]		

	return transposed

def matrixMulitply(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2): 
		return 

	resultMatrix = []

	for row in matrix1:
		resultRow = []

		for column in transpose(matrix2):
			value = dotProduct(row, column)
			resultRow.append(value)

		resultMatrix.append(resultRow)	

	return resultMatrix

def ReLU(matrix):
    return [[max(0, x) for x in row] for row in matrix]

def softmax(matrix):
	result = []
	for vector in matrix:
		maximum = max(vector)

		exponentials = [E**(x - maximum) for x in vector]
		total = sum(exponentials)
	    
		result.append([exponential / total for exponential in exponentials])
	return result

def catergoricalCrossEntropy(yPredicted, yTrue):
	samples = len(yPredicted)

	#prevents -np.log(0) and stops mean being dragged to any value
	clippedPredictions = clip(yPredicted, 1e-7, 1 - 1e-7) 
	#correctConfidences = clippedPredictions[range(samples), y_true] - it's a list, not an numpy array!

#-------------------------
#--------CLASSES----------
#-------------------------
class Layer:
	def __init__(self, weights, biases, activationFunction):
		self.weights = weights
		self.biases = biases
		self.activationFunction = activationFunction
		self.weightedOutput = []
		self.activatedOutput = []

	def forward(self, inputs):
		self.weightedOutput = matrixMulitply(inputs, transpose(self.weights))
		self.weightedOutput = addBiases(self.weightedOutput, self.biases)
		self.activatedOutput = self.activationFunction(self.weightedOutput)
		

class Network:
	def __init__(self):
		self.layers = []

	def addLayer(self, layer):
		self.layers.append(layer)

	def forward(self, inputs):
		for layer in self.layers:
			layer.forward(inputs)





firstLayer = Layer([[2,3],[1,2],[-0.1,1]], [0.5, 0.5], ReLU)
firstLayer.forward(X)
print(firstLayer.activatedOutput)
