def merge(arr,first,middle,last):
    arr1 = arr[first:middle+1]
    arr2 = arr[middle+1:last+1]
    i = 0
    j = 0
    k = first 

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
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
        arr[k] = arr2[j]
        k+=1
        j+=1



def mergeSort(arr,first,last):
    if first<last:
        middle = (first+last)//2
        mergeSort(arr,first,middle)
        mergeSort(arr,middle+1,last)
        merge(arr,first,middle,last)


arr = [5,4,3,1,7,8,2]
mergeSort(arr,0,len(arr)-1)
print(*arr)
