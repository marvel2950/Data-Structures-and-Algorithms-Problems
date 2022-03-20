def linearSearch(arr,ele):
    ind = -1
    for i in range(0,len(arr)):
        if arr[i]==ele:
            ind = i
            break 
    return ind

arr = [1,0,55,6,2,7]
ele = 6
index = linearSearch(arr,ele)
print(index)