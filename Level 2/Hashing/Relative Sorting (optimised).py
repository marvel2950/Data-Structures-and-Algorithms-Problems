from collections import Counter

def sortRelative(arr1,arr2):
    res = []
    f = Counter(arr1)

    for i in arr2:
        res.extend([i]*f[i])
        f[i] = 0
    rem = list(sorted((filter(lambda x:f[x] != 0,f.keys()))))
    for i in rem:
        res.extend([i]*f[i])
    return res

arr1 = [2,1,2,5,7,1,9,3,6,8,8]
arr2 = [2,1,8,3]
res = sortRelative(arr1,arr2)
print(res)