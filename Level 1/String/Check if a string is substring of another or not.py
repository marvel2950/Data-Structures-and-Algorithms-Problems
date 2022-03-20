def isSubstring1(s1,s2):
    m = len(s1)
    n = len(s2)
    for i in range(n-m+1):
        for j in range(m):
            if s2[i+j]!=s1[j]:
                break 
        if j+1==m:
            return i 
    return -1

s1 = "euro"
s2 = "ineuron"
flag = isSubstring1(s1,s2)
print(flag)

def isSubstring2(s1,s2):
    t = 0
    l = len(s1)
    i = 0
    for i in range(l):
        if t==len(s2):
            break
        if s1[i]==s2[t]:
            t+=1 
        else:
            t = 0
    if t<len(s2):
        return -1
    return i-t

s1 = "euro"
s2 = "ineuron"
flag = isSubstring2(s2,s1)
print(flag)