def insertionSort(arr):
    for i in range(len(arr)):
        j = i-1
        while j>=0 and arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j-=1

arr = [5,4,3,2,1]
insertionSort(arr)
print(arr)