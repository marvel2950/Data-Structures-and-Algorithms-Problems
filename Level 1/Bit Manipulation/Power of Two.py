import math
def isPowerOfTwo1(x):
    if x==0:
        return False
    while x%2==0:
        x=x/2 
    if x==1:
        return True 
    return False 

x = 0
flag = isPowerOfTwo1(x)
print(flag)

def log2(x):
    if x==0:
        return False 
    return math.log10(x)/math.log10(2)

def isPowerOfTwo2(x):
    if math.ceil(log2(x))==math.floor(log2(x)):
        return True 
    return False 

x = 10
flag = isPowerOfTwo2(x)
print(flag)

def isPowerOfTwo2(x):
    if x&(x-1)==0:
        return True 
    return False 

x = 32
flag = isPowerOfTwo2(x)
print(flag)