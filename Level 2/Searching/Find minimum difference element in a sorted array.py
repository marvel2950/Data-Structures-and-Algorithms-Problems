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

def floor(arr,ele,start,end):
    res = -1
    while start <= end:
        mid = (start+end)//2
        if ele==arr[mid]:
            res = ele
            break
        elif ele<arr[mid]:
            end = mid-1
        elif ele>arr[mid]:
            res = arr[mid]
            start = mid+1 
    return res

def ceil(arr,ele,start,end):
    res = -1
    while start <= end:
        mid = (start+end)//2
        if ele==arr[mid]:
            res = ele
            break
        elif ele>arr[mid]:
            start = mid+1
        elif ele<arr[mid]:
            res = arr[mid]
            end = mid-1 
    return res

def minDiffEle(arr,ele):
    start = 0
    end = len(arr)-1
    ind = binarySearch(arr,ele,start,end)
    if ind != -1:
        return arr[ind]
    floorValue = floor(arr,ele,start,end)
    #print(floorValue)
    ceilValue = ceil(arr,ele,start,end)
    #print(ceilValue)
    floorBeta = abs(floorValue-ele)
    ceilBeta = abs(ceilValue-ele)
    if floorBeta > ceilBeta:
        return ceilValue
    else:
        return floorValue

arr = [4,6,9,12]
ele = 8
val = minDiffEle(arr,ele)
print(val)
