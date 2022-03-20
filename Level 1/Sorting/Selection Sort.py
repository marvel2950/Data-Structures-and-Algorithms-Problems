def selectionSort(arr):
    for i in range(len(arr)):
        fixed = i
        for j in range(i+1,len(arr)):
            if arr[fixed]>arr[j]:
                arr[fixed],arr[j] = arr[j],arr[fixed]

arr = [5,4,3,2,1]
selectionSort(arr)
print(arr)