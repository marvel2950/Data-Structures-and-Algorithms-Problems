def fibonacci1(n):
    arr = [0, 1]
    for i in range(2,n):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n - 1]

def fibonacci2(n):
    x = 0
    y = 1
    if n == 0:
        return x
    elif n == 1:
        return y
    for i in range(2,n):
        z = x + y
        x = y
        y = z
    return z

def fibonacci3(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibonacci3(n-1)+fibonacci3(n-2)

print(fibonacci1(5))
print(fibonacci2(5))
print(fibonacci3(5))