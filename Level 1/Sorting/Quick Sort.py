def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1 
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pivotPos = partition(arr,low,high)
        quickSort(arr,low,pivotPos-1)
        quickSort(arr,pivotPos+1,high)



arr = [2,5,1,4,3]
quickSort(arr,0,len(arr)-1)
print(arr)