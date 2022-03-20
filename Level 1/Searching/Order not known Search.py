def binarySearchDescending(arr,ele,start,end):
    ind = -1
    while start <=end:
        mid = start+ (end-start)//2
        if arr[mid]==ele:
            ind = mid
            break
        elif ele>arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind

def binarySearchAscending(arr,ele,start,end):
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

def binarySearch(arr,ele,start,end):
    if len(arr)==1:
        if ele==arr[0]:
            return 0
        return -1 
    elif arr[0]<arr[-1]:
        return binarySearchAscending(arr,ele,start,end)
    elif arr[0]>arr[-1]:
        return binarySearchDescending(arr,ele,start,end)

arr = [1,2,3,4]
ele = 99
start = 0
end = len(arr)-1
index = binarySearch(arr,ele,start,end)
print(index)