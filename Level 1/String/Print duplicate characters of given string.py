def duplicateChar1(ip_str):
    count = []
    for i in list(set(ip_str)):
        c = 0
        for j in ip_str:
            if i==j:
                c+=1 
        count.append([i,c])
    
    ans = []
    for char,c in count:
        if c>1:
            ans.append(char)
    return ans

ip_str = 'abcabaaa'
duplicateList = duplicateChar1(ip_str)
print(duplicateList)


def duplicateChar2(ip_str):
    count = {}
    for i in ip_str:
        if i in count:
            count[i]=count[i]+1 
        else:
            count[i] = 1
    ans = []
    for char,c in count.items():
        if c>1:
            ans.append(char)
    return ans

ip_str = 'abcabaaa'
duplicateList = duplicateChar2(ip_str)
print(duplicateList)