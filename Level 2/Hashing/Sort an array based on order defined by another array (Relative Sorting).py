def firstOccurence(arr,ele,start,end):
    ind = -1
    while start <= end:
        mid = (start+end)//2
        if ele==arr[mid]:
            ind = mid
            end = mid-1
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind

def sortRelative(arr1,arr2):
    m = len(arr1)
    n = len(arr2)

    temp = [0]*m
    vis = [0]*m

    for i in range(0,m):
        temp[i] = arr1[i]
    temp.sort()

    ind = 0
    for i in range(0,n):
        f = firstOccurence(temp,arr2[i],0,m-1)
        if f==-1:
            continue 
        j = f 
        while j<m and temp[j]==arr2[i] and vis[j]==0:
            arr1[ind] = temp[j]
            ind += 1
            vis[j] = 1
            j += 1

    for i in range(0,m):
        if vis[i]==0:
            arr1[ind] = temp[i]
            ind += 1

arr1 = [2,1,2,5,7,1,9,3,6,8,8]
arr2 = [2,2,1,8,3]
sortRelative(arr1,arr2)
print(arr1)