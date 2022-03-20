def firstOccurence(arr,ele,start,end):
    ind = -1
    while start <= end:
        mid = (start+end)//2
        if ele==arr[mid]:
            ind = mid
            end = mid-1
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind

def lastOccurence(arr,ele,start,end):
    ind = -1
    while start <= end:
        mid = (start+end)//2
        if ele==arr[mid]:
            ind = mid
            start = mid+1
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind


arr = [0,1,1,5,5,5,7,7,7]
ele = 5
start = 0
end = len(arr)-1
firstOccur = firstOccurence(arr,ele,start,end)
print(firstOccur)
lastOccur = lastOccurence(arr,ele,start,end)
print(lastOccur)