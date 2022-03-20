def sort012(arr):
    arr.sort() #=> Inplace

def sort012(arr):
    count0 = 0
    count1 = 0 
    for i in arr:
        if i==0:
            count0=count0+1 
        elif i==1:
            count1=count1+1
    for i in range(0,count0):
        arr[i] = 0 
    for i in range(count0,count1+count0):
        arr[i] = 1 
    for i in range(count1+count0,len(arr)):
        arr[i] = 2


def sort012(arr):
    lo = 0
    hi = len(arr)-1 
    mid = 0
    while mid<=hi:
        if arr[mid]==0:
            arr[lo],arr[mid] = arr[mid],arr[lo]
            lo+=1 
            mid+=1
        elif arr[mid]==1:
            mid=mid+1 
        else:
            arr[mid],arr[hi] = arr[hi],arr[mid]
            hi = hi-1 
    return arr

arr = [1,1,2,2,1,0,2,1,1,0,2,0,1,1]
sort012(arr)
print(arr)