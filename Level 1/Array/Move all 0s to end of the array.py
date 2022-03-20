def zeroesToEnd1(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]==0:
            arr[i],arr[j] = arr[j],arr[i]
            j-=1 
        else:
            i+=1

arr = [-5,0,1,0,4,-0,-7,8,9,10]
zeroesToEnd1(arr)
print(arr)

def zeroesToEnd2(arr):
    i = 0
    alpha = []
    while i<len(arr):
        if arr[i]==0:
            alpha.append(arr[i])
            arr.pop(i)
        else:
            i+=1 
    for i in alpha:
        arr.append(i)

arr = [-5,0,1,0,4,-0,-7,8,9,10]
zeroesToEnd2(arr)
print(arr)

def zeroesToEnd3(arr):
    i = 0
    for j in range(len(arr)):
        if arr[i]==0:
            alpha = arr.pop(i)
            arr.append(alpha)
        else:
            i+=1 

arr = [-5,0,1,0,4,-0,-7,8,9,10]
zeroesToEnd3(arr)
print(arr)