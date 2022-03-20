def longestUniqueSubstring(str):
    seen = {}
    maxLength = 0
    start = 0
    for end in range(len(str)):
        if str[end] in seen:
            start = max(start,seen[str[end]]+1)
        seen[str[end]] = end
        maxLength = max(maxLength,end-start+1)
    return maxLength

str = "ABDEFGABEF"
lenStr = longestUniqueSubstring(str)
print(lenStr)