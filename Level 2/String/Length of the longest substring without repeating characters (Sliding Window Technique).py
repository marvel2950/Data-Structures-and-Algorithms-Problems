def longestUniqueSubstring(str):
    n = len(str)
    maxLength = 0
    for i in range(n):
        vis = [0]*256
        for j in range(i,n):
            if vis[ord(str[j])]:
                break
            else:
                maxLength = max(maxLength,j-i+1)
                vis[ord(str[j])] = True 
        vis[ord(str[i])] = False 
    return maxLength

def longestUniqueSubstring(str):
    n = len(str)
    res = ''
    maxLength = -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for cur in str:
        if cur in res:
            res = res[res.index(cur)+1:]
        res = res+cur 
        maxLength = max(maxLength,len(res))
    return maxLength

str = "ABDEFGABEF"
lenStr = longestUniqueSubstring(str)
print(lenStr)