def countSort(arr,b,k):
    count = [0]*(k+2)
    for i in arr:
        count[i] = count[i]+1 
    for i in range(1,k+1):
        count[i] = count[i-1]+count[i]

    for i in range(len(arr)-1,-1,-1):
        b[count[arr[i]]-1] = arr[i]
        count[arr[i]] = count[arr[i]]-1


arr = [3,2,3,2,3,4,1,1]
k = max(arr)
b = [0]*len(arr)
countSort(arr,b,k)
print(b)