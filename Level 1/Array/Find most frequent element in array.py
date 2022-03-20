import sys
def mostFreqEle1(arr):
    count = []
    for i in list(set(arr)):
        c = 0
        for j in arr:
            if i==j:
                c=c+1 
        count.append([i,c])
    #print(count)
    max = -sys.maxsize
    ans = -1 
    for nu,cou in count:
        if cou>max:
            max = cou 
            ans = nu 
    return ans


arr = [1,1,2,2,3,3,4,4,1,1,1,5,6,5,6]
opEle = mostFreqEle1(arr)
print(opEle)

import sys
def mostFreqEle2(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1 
        else:
            count[i]=count[i]+1

    print(count)
    max = -sys.maxsize
    ans = -1 
    for nu,cou in count.items():
        if cou>max:
            max = cou 
            ans = nu 
    return ans


arr = [1,1,2,2,3,3,4,4,1,1,1,5,6,5,6]
opEle = mostFreqEle2(arr)
print(opEle)