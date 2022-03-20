def fib(n):
    if n<=1:
        return n 
    else:
        return fib(n-1)+fib(n-2)

def ways(s):
    return fib(s+1)

s = 4
print(ways(s))