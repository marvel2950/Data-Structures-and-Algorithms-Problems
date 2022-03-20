import random
def listInit():
    l = []
    for i in range(1,101):
        l.append(i)
    missingIndex = random.randint(0,99)
    print("Popped element",l[missingIndex])
    l.pop(missingIndex)
    return l

def missingEle1(arr):
    ele = -1 
    for i in range(1,101):
        if i not in arr:
            ele = i 
            break 
    return ele


arr = listInit()
ele = missingEle1(arr)
print("Answer",ele)


def missingEle2(arr):
    ele = -1 
    ins = {}
    for i in arr:
        ins[i] = True
    for i in range(1,101):
        if i not in ins:
            ele = i 
            break 
    return ele


ele = missingEle2(arr)
print("Answer",ele)

def missingEle3(arr):
    exp_sum = 100*101//2
    #actual_sum = sum(arr)
    actual_sum = 0
    for i in arr:
        actual_sum=actual_sum+i
    ele = exp_sum-actual_sum
    return ele


ele = missingEle3(arr)
print("Answer",ele)