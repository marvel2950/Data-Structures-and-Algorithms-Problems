def equilibrium(arr):
	for i in range(0,len(arr)):
		leftSum = 0
		rightSum = 0
		for j in range(0,i):
			leftSum = leftSum+arr[j]
		for j in range(i+1,len(arr)):
			rightSum = rightSum+arr[j]
		if leftSum == rightSum:
			return i
	return -1

def equilibrium(arr):
	leftSum = 0
	rightSum = 0
	for i in range(len(arr)):
		rightSum = rightSum+arr[i]
	for i in range(0,len(arr)):
		rightSum = rightSum-arr[i]
		if leftSum == rightSum:
			return i
		leftSum = leftSum+arr[i]
	return -1

arr = [-7,1,5,2,-4,3,0]
point = equilibrium(arr)
print(point)
