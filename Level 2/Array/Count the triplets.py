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

def tripletSum(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(0,n):
                if i!=j!=k and arr[i] == arr[j]+arr[k]:
                    print(arr[i],arr[j],arr[k])

def tripletSum(arr):
    n = len(arr)
    arr.sort(reverse = True)
    for i in range(0,n):
        if twoSum2(arr[i+1:n],arr[i]) == True:
            return True
    return False
  
arr =[5,32,1,7,10,50,19,21,2]
count = tripletSum(arr)
print(count)