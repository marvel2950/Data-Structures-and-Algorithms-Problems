def substring1(str):
    subList = []
    n = len(str)
    for i in range(n):
        for j in range(i+1,n+1):
            alpha = []
            for k in range(i,j):
                alpha.append(str[k])
            alpha = ''.join(alpha)
            subList.append(alpha)
    return subList

str= "abc"
subList = substring1(str)
print(subList)

def substring2(str):
    subList = []
    n = len(str)
    for i in range(n):
        for j in range(i+1,n+1):
            subList.append(str[i:j])
    return subList

str= "abc"
subList = substring2(str)
print(subList)

def substring3(str):
    subList = []
    n = len(str)
    for i in range(n):
        temp = []
        for j in range(i,n):
            temp.append(str[j])
            alpha = ''.join(temp)
            subList.append(alpha)
    return subList

str= "abc"
subList = substring3(str)
print(subList)