def binarySearch(arr,ele,start,end):
    ind = -1
    while start <=end:
        mid = start+ (end-start)//2
        if arr[mid]==ele:
            ind = mid
            break
        elif ele<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return ind

def search1(mat,target):
    i = 0
    j = 0
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == target:
                return [i,j]
    return -1

def search2(mat,target):
    for i in range(len(mat)):
        ind = binarySearch(mat[i],target,0,len(mat[i])-1)
        if ind!=-1:
            return [i,ind]
    return -1

def search3(mat,target):
    n = len(mat)
    m = len(mat[0])
    i = 0
    j = m-1
    while i<n and j>=0:
        if mat[i][j]==target:
            return [i,j]
        elif mat[i][j]>target:
            j-=1 
        else:
            i+=1 
    return -1

mat = [ 
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
      ]
target = 110

ind = search1(mat,target)
print(ind)
ind = search2(mat,target)
print(ind)
ind = search3(mat,target)
print(ind)