def eleOccursOnce(arr):
    xor_val = 0
    for i in arr:
        xor_val=xor_val^i 
    ele = xor_val
    return ele

arr = [1,1,2,3,4,3,2,5,6,7,8,7,6,8,4]
print(sorted(arr))
ele = eleOccursOnce(arr)
print(ele)