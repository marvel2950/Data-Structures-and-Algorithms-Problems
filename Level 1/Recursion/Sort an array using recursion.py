def insert(arr,alpha):
    if len(arr)==0 or arr[-1]<alpha:
        arr.append(alpha)
        return
    val = arr.pop(-1)
    insert(arr,alpha)
    arr.append(val)

def sort(arr):
    if len(arr)==1:
        return
    alpha = arr.pop(-1)
    sort(arr)
    insert(arr,alpha)

arr = [1,0,3,8,2,5]
sort(arr)
print(arr)