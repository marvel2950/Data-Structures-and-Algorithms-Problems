def binarySearch(arr,ele,start,end):
    ind = -1
    while start <=end:
        mid = start+ (end-start)//2
        if arr[mid]==ele:
            ind = mid
            break
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind

def isSubset(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    for i in range(n):
        check = True
        for j in range(m):
            if arr2[i] == arr1[j]:
                check = False
                break
        if check:
            return False 
    return True

def isSubset(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    arr1.sort()
    for i in range(n):
        if binarySearch(arr1,arr2[i],0,m-1)==-1:
            return False
    return True

def isSubset(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    hashset = {}
    for i in range(m):
        hashset[arr1[i]] = True
    for i in range(n):
        if arr2[i] not in hashset:
            return False
    return True

arr1 = [11,1,13,21,3,7]
arr2 = [11,3,7,1]

arr1 = [10,5,2,23,19]
arr2 = [19,5,3]

flag = isSubset(arr1,arr2)
print(flag)