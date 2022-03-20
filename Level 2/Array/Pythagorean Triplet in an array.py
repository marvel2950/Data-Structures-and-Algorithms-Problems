def twoSum2(arr,sum):
	low = 0
	high = len(arr)-1
	arr.sort()
	while low<high:
		if arr[low]+arr[high]==sum:
			return True
		if arr[low]+arr[high]>sum:
			high-=1 
		else:
			low = low+1
	return False

def pythagoreanTriplet(arr):
    n = len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]*arr[i]+arr[j]*arr[j]==arr[k]*arr[k]:
                    print(arr[i],arr[j],arr[k])
                    return True
    return False

def pythagoreanTriplet(arr):
    n = len(arr)
    for i in range(len(arr)):
        arr[i] = arr[i]*arr[i]
    arr.sort(reverse=True)
    print(arr)
    for i in range(0,n):
        if twoSum2(arr[i+1:n],arr[i]) == True:
            return True
    return False
  
arr = [3,1,4,6,5]
flag = pythagoreanTriplet(arr)
print(flag)