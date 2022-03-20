def inversionCount(arr):
    count = 0 
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                print(arr[i],arr[j])
                count+=1 
    return count

arr = [1,20,6,4,5]
count = inversionCount(arr)
print(count)

def merge(arr,first,middle,last):
    arr1 = arr[first:middle+1]
    arr2 = arr[middle+1:last+1]
    i = 0
    j = 0
    k = first 
    count = 0

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            arr[k] = arr1[i]
            i+=1 
            k+=1
        else:
            count+=(middle-i+1)
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

    return count

def mergeSort(arr,first,last):
    count = 0
    if first<last:
        middle = (first+last)//2
        count += mergeSort(arr,first,middle)
        count += mergeSort(arr,middle+1,last)
        count += merge(arr,first,middle,last)

    return count

arr = [1,20,6,4,5]
count = mergeSort(arr,0,len(arr)-1)
print(count)