def binarySearch(arr,ele,start,end):
    if end >= start:
        mid = (start + end)//2
        if arr[mid] == ele:
            return mid 
        elif arr[mid]>ele:
            return binarySearch(arr,ele,start,mid-1)
        else:
            return binarySearch(arr,ele,mid+1,end)
    else:
        return -1

arr = [1,2,5,6,9,14]
ele = 9 
start = 0 
end = len(arr)-1
ind = binarySearch(arr,ele,start,end)
print(ind)