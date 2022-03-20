def reverse(arr,f,l):
    if f<l:
        arr[f],arr[l] = arr[l],arr[f]
        l=l-1
        f=f+1 
        reverse(arr,f,l)

def merge(arr,first,middle,last):
    i = first
    j = middle+1

    while i<=middle and arr[i]<0:
        i+=1 
    while j<=last and arr[j]<0:
        j+=1 

    # arr[first:i] -> negative (Ln)
    # arr[i:middle] -> positive (Lp)
    # arr[middle:j] -> negative (Rn)
    # arr[j:last] -> positive (Rp)

    reverse(arr,i,middle) # (Lp`)
    reverse(arr,middle+1,j-1) # (Rn`)

    reverse(arr,i,j-1) #(Lp`` Rn ``)

    # arr-> LnRnLpRp

def mergeSort(arr,first,last):
    if first<last:
        middle = (first+last)//2
        mergeSort(arr,first,middle)
        mergeSort(arr,middle+1,last)
        merge(arr,first,middle,last)

arr = [-5,0,1,2,4,-6,-7,8,9,10]
mergeSort(arr,0,len(arr)-1)
print(*arr)
