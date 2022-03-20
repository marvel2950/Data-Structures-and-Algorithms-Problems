def segregate0And1(arr):
    arr.sort()

def segregate0And1(arr):
    count = 0 
    for i in arr:
        if i==0:
            count = count+1 
    for i in range(count):
        arr[i] = 0 
    for i in range(count,len(arr)):
        arr[i] = 1 


def segregate0And1(arr):
    left = 0
    right = len(arr)-1 
    while left<right:
        while arr[left] == 0 and left<right:
            left+=1
        while arr[right] == 1 and left<right:
            right-=1 
        if left<right:
            arr[left] = 0
            arr[right] = 1 
            left+=1 
            right-=1


def segregate0And1(arr):
    left = 0
    right = len(arr)-1 
    while left<right:
        if arr[left]==1:
            arr[left],arr[right] = arr[right],arr[left]
            right-=1 
        else:
            left+=1

arr = [1,1,0,1,1,0,0,1]
segregate0And1(arr)
print(arr)