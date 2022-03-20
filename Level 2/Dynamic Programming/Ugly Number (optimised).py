def nthUglyNum(n):
    ugly = [0]*n
    ugly[0] = 1
    i2 = 0
    i3 = 0
    i5 = 0
    next2 = 2
    next3 = 3
    next5 = 5

    for i in range(1,n):
        ugly[i] = min(next2,next3,next5)

        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2]*2
        
        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5]*5

        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3]*3

    return ugly[n-1]

n = 10
num = nthUglyNum(n)
print(num)