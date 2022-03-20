from collections import defaultdict

def frequencySort(arr):
	d = defaultdict(lambda:0)
	for i in range(len(arr)):
		d[arr[i]] += 1
	arr.sort(key=lambda x:(-d[x],x))

arr = [8,7,8,7,8,5,4]
frequencySort(arr)
print(arr)