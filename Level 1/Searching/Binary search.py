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

arr = [1,2,5,6,9,14]
ele = 99
start = 0
end = len(arr)-1
index = binarySearch(arr,ele,start,end)
print(index)