import random

def listInit():
    l = []
    for i in range(1,101):
        l.append(i)
    missingIndex = random.randint(0,99)
    print("Popped element",l[missingIndex])
    l.pop(missingIndex)
    return l

def missingEle(arr):
    exp_xor = 0
    actual_xor = 0
    for i in range(1,101):
        exp_xor=exp_xor^i 
    for i in arr:
        actual_xor = actual_xor^i 
    ele = actual_xor^exp_xor
    return ele

arr = listInit()
ele = missingEle(arr)
print("Answer",ele)