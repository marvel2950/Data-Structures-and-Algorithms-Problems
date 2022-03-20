def leaders(arr):
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]<arr[j]:
				break 
		if j==len(arr)-1:
			print(arr[i])

def leaders(arr):
	n = len(arr)
	max = arr[n-1]
	print(max)
	for i in range(n-2,-1,-1):
		if max<arr[i]:
			print(arr[i])
			max = arr[i]

arr = [16,17,4,3,5,2]
leaders(arr)