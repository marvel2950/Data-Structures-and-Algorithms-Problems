def sortedOrNot1(arr):
    if len(arr)==0 or len(arr)==1:
        return True 
    return arr[0]<arr[1] and sortedOrNot1(arr[1:])

arr = [1,2,5,7,8]
flag = sortedOrNot1(arr)
print(flag)

def sortedOrNot2(arr):
    if len(arr)==0 or len(arr)==1:
        return True 
    n = len(arr)
    return arr[n-2]<arr[n-1] and sortedOrNot2(arr[0:n-1])

arr = [1,2,5,7,8]
flag = sortedOrNot2(arr)
print(flag)

def sortedOrNot3(arr):
    if len(arr)==0 or len(arr)==1:
        return True 
    n = len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            return False 
    return True
    
arr = [1,2,5,100,7,8]
flag = sortedOrNot3(arr)
print(flag)