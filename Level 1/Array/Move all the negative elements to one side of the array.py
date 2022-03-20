def segregateNegative1(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]<0:
            arr[i],arr[j] = arr[j],arr[i]
            j-=1 
        else:
            i+=1

arr = [-5,0,1,2,4,-6,-7,8,9,10]
segregateNegative1(arr)
print(arr)

def segregateNegative2(arr):
    i = 0
    alpha = []
    while i<len(arr):
        if arr[i]<0:
            alpha.append(arr[i])
            arr.pop(i)
        else:
            i+=1 
    for i in alpha:
        arr.append(i)

arr = [-5,0,1,2,4,-6,-7,8,9,10]
segregateNegative2(arr)
print(arr)