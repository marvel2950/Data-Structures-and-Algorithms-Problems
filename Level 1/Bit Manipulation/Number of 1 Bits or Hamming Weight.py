def countOne(n):
    bin_num = bin(n)[2:]
    count = 0
    for i in bin_num:
        if i=='1':
            count+=1 
    return count

n = 23
oneBits = countOne(n)
print(oneBits)

def countOne2(n):
    count = 0
    while n:
        n = n&(n-1)
        count+=1 
    return count

n = 23
oneBits = countOne2(n)
print(oneBits)