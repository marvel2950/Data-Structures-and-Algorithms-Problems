def powerOfTwo(n):
    if n==0:
        return 1
    elif n%2==0:
        return powerOfTwo(n//2)*powerOfTwo(n//2)
    else:
        return 2*powerOfTwo(n//2)*powerOfTwo(n//2)
print(powerOfTwo(5))