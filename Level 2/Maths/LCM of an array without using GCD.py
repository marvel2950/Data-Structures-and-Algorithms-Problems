def lcmArray(arr):
	n = len(arr)
	maxNum = max(arr)
	res = 1
	x = 2
	while x <= maxNum:
		ind = []
		for j in range(n):
			if arr[j] % x == 0:
				ind.append(j)
		if len(ind) >= 2:
			for j in range(len(ind)):
				arr[ind[j]] = arr[ind[j]] // x
			res = res * x
		else:
			x += 1
	for i in range(n):
		res = res * arr[i]

	return res

arr = [1, 2, 3, 4, 28]
lcmVal = lcmArray(arr)
print(lcmVal)