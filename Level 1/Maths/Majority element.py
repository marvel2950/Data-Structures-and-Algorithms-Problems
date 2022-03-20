import math
def majorityEle1(arr):
    for i in list(set(arr)):
        c = 0
        for j in arr:
            if i==j:
                c+=1 
                if c>math.floor(len(arr)/2):
                    return i 

arr = [1,1,2,2,3,3,4,4,1,1,1,1,1]
opEle = majorityEle1(arr)
print(opEle)

def majorityEle2(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1 
        else:
            count[i] = count[i]+1
            if count[i]>math.floor(len(arr)/2):
                return i 

arr = [1,1,2,2,3,3,4,4,1,1,1,1,1]
opEle = majorityEle2(arr)
print(opEle)

def majorityEle3(arr):
    count = 0
    ele = -1
    for i in arr:
        if count==0:
            ele = i 
        if ele == i:
            count+=1 
        else:
            count-=1
    return ele 

arr = [1,1,2,2,3,3,4,4,1,1,1,1,1]
opEle = majorityEle3(arr)
print(opEle)