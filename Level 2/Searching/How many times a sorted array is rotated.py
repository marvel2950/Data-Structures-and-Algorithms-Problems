def pivot(arr,start,end):
    n = len(arr)
    res = -1
    while start <= end:
        mid = (start+end)//2
        prev = (mid+n-1)%n
        next = (mid+1)%n 
        if arr[mid]<=arr[next] and arr[mid]<=arr[prev]:
            res = mid 
            break
        elif arr[start] < arr[mid]:
            start = mid+1
        elif arr[end]>arr[mid]:
            end = mid-1 
    return res 

def timesRotated(arr):
    start = 0
    end = len(arr)-1
    pivotIndex = pivot(arr,start,end)
    #print(pivotIndex)
    times = len(arr)-pivotIndex
    return times
    
arr = [8,11,12,15,18,2,5,6]
times = timesRotated(arr)
print(times)
