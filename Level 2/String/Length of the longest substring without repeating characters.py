def areDistinct(str,i,j):
    visited = [0]*26
    for k in range(i,j+1):
        if visited[ord(str[k])-ord('A')]:
            return False
        visited[ord(str[k])-ord('A')] = True 
    return True

def longestUniqueSubstring(str):
    n = len(str)
    maxLength = 0
    for i in range(n):
        for j in range(i,n):
            if areDistinct(str,i,j):
                maxLength = max(maxLength,j-i+1)
    return maxLength

str = "ABDEFGABEF"
lenStr = longestUniqueSubstring(str)
print(lenStr)