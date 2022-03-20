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

arr = [1,2,3,4,8,10,11,12]
ele = 6
start = 0
end = len(arr)-1
floorValue = floor(arr,ele,start,end)
print(floorValue)
ceilValue = ceil(arr,ele,start,end)
print(ceilValue)