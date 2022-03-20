def merge(arr1,arr2):
    arr = [-1]*(len(arr1)+len(arr2)) #=> [-1,-1,-1,-1,-1,-1,-1,-1]
    i = 0
    j = 0 
    k = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k] = arr1[i]
            i+=1 
            k+=1
        else:
            arr[k] = arr2[j]
            j+=1
            k+=1 
    while i<len(arr1):
        arr[k] = arr1[i]
        i+=1 
        k+=1
    while j<len(arr2):
        arr[k] = arr2[i]
        j+=1 
        k+=1
    return arr

arr1 = [1,6,8,11,15]
arr2 = [2,3,7]
arr = merge(arr1,arr2)
print(arr)