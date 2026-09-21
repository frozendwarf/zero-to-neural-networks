#NNFS-3 Matrix Multiplcation

matrixA = [
	[1, 2, 3],
	[2, 2, 2],
	[1, 1, 1],
	[1, 2, 1]
]

matrixB = [
	[2, 3, 0, 2],
	[3, 1, 4, 3],
	[5, 0, 1, 2],

]

a = [1,2,3]

b = [4,5,6]


def dotProduct(list1, list2):
	output = 0
	for i in range(len(list1)):
		output += list1[i] * list2[i]
	return output

def transpose(array):
	rows = len(array)
	columns = len(array[0])
	transposed = [[None] * rows for _ in range(columns)]

	for i, row in enumerate(array):
		for j, value in enumerate(row):
			transposed[j][i] = array[i][j]		

	return transposed

print(transpose(matrixB)
)