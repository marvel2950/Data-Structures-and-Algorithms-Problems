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

def tripletSum(arr,sum):
    n = len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == sum:
                    print(arr[i],arr[j],arr[k])
                    return True
    return False

def tripletSum(arr,sum):
    n = len(arr)
    hash = {}
    for i in range(0,n):
        for j in range(i+1,n):
            temp = sum-arr[i]-arr[j]
            if temp in hash:
                print(arr[i],arr[j],sum-arr[i]-arr[j])
                return True 
            hash[arr[i]] = True
    return False

def tripletSum(arr,sum):
    n = len(arr)
    arr.sort()
    for i in range(0,n-2):
        if twoSum2(arr[i+1:n],sum-arr[i]) == True:
            return True
    return False
  
arr =[1,4,45,6,10,8]
sum = 22
isThere = tripletSum(arr,sum)
print(isThere)