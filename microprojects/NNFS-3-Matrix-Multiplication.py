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
	#(1,n) -> (n,1) and vice versa
	transposed = []
	if len(array) == 1:
		for x in array[0]:
			transposed.append([x])
	return transposed

print(transpose([a]))
