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


def searchingOneInInfiniteSortedArray(arr,ele):
    start = 0
    end = 1
    while ele > arr[end]:
        start = end
        end = end*2
    ind = firstOccurence(arr,ele,start,end)
    return ind


arr = [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
ele = 1
index = searchingOneInInfiniteSortedArray(arr,ele)
print(index)
