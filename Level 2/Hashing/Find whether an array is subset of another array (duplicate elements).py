def isSubset(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    if m<n:
        return False 
    arr1.sort()
    arr2.sort()
    print(arr1,arr2)

    while i<n and j<m:
        if arr1[j]<arr2[i]:
            j+=1 
        elif arr1[j] == arr2[i]:
            i+=1
            j+=1
        elif arr1[j]>arr2[i]:
            return False 
    if i<n:
        return False
    else:
        return True

def isSubset(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    hashset = {}
    for i in range(m):
        if arr1[i] in hashset:
            hashset[arr1[i]] += 1
        else:
            hashset[arr1[i]] = 1
    for i in range(n):
        if arr2[i] in hashset and hashset[arr2[i]]>0:
            hashset[arr1[i]] -= 1
        else:
            return False
    return True

arr1 = [11,1,3,13,21,7]
arr2 = [11,3,7,1,3]

flag = isSubset(arr1,arr2)
print(flag)