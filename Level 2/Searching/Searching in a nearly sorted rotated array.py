def searchNearlySorted(arr,ele,start,end):
    ind = -1
    while start<=end:
        mid = (start+end)//2 
        if arr[mid] == ele:
            ind = mid
            break 
        elif mid+1<=end and arr[mid+1] == ele:
            ind = mid+1
            break 
        elif mid-1>=start and arr[mid-1] == ele:
            ind = mid-1
            break 
        elif ele<arr[mid-1]:
            end = mid-2
        else:
            start = mid+2
    return ind

arr = [5,10,30,20,40]
ele = 20 
start = 0
end = len(arr)-1 
ind = searchNearlySorted(arr,ele,start,end)
print(ind)