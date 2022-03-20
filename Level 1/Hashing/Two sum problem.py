def twoSum1(arr,sum):
	pairs = []
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j]==sum:
				pairs.append([arr[i],arr[j]])
	return pairs

arr = [1,5,7,-1,5]
sum = 6
pairs = twoSum1(arr,sum)
print(pairs)

def twoSum2(arr,sum):
	pairs = []
	low = 0
	high = len(arr)-1
	arr.sort()
	while low<high:
		if arr[low]+arr[high]==sum:
			pairs.append([arr[low],arr[high]])
		if arr[low]+arr[high]>sum:
			high-=1 
		else:
			low = low+1
	return pairs

arr = [1,5,7,-1,5]
sum = 6
pairs = twoSum2(arr,sum)
print(pairs)

def twoSum3(arr,sum):
	pairs = []
	hash = dict()
	for i in range(0,len(arr)):
		temp = sum-arr[i]
		if temp in hash:
			count = hash[temp]
			for j in range(count):
				pairs.append([temp,arr[i]])
		if arr[i] in hash:
			hash[arr[i]]+=1
		else:
			hash[arr[i]] = 1
	return pairs

arr = [1,5,7,-1,5]
sum = 6
pairs = twoSum(arr,sum)
print(pairs)