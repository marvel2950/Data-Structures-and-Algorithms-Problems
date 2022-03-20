def searchingInInfiniteSortedArray(arr,ele):
    start = 0
    end = 1
    while ele > arr[end]:
        start = end
        end = end*2
    ind = binarySearch(arr,ele,start,end)
    return ind

def binarySearch(arr,ele,start,end):
    ind = -1
    while start <= end:
        mid = (start+end)//2
        if ele==arr[mid]:
            ind = mid 
            break 
        elif ele<arr[mid]:
            end = mid-1
        else:
            start=mid+1
    return ind

arr = [1,2,3,5,6,9,14,15,17,18,19,20,21,22,24,26,27,28,29]
ele = 9
index = searchingInInfiniteSortedArray(arr,ele)
print(index)
