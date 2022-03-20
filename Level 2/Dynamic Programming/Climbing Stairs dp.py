def waysUtil(n):
    res = [0 for x in range(n)]
    res[0] = 1
    res[1] = 1

    for i in range(2,n):
        j = 1
        while j<=2 and j<=i:
            res[i] = res[i]+res[i-j]
            j = j+1
    return res[n-1]

def ways(s):
    return waysUtil(s+1)

s = 4
print(ways(s))