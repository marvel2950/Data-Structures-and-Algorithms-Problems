def fact(n):
    res = 1
    for i in range(1,n+1):
        res = res*i 
    return res 

def nCr(n,r):
    return fact(n)// (fact(r)*fact(n-r))

def uniquePaths1(i,j,x,y):
    if i==x-1 and j==y-1:
        return 1 
    elif i>=x or j>=y:
        return 0
    else:
        return uniquePaths1(i+1,j,x,y)+uniquePaths1(i,j+1,x,y)

def uniquePaths2(i,j,x,y,dp):
    if i==x-1 and j==y-1:
        dp[i][j] = 1
        return 1 
    elif i>=x or j>=y:
        dp[i][j] = 0
        return 0
    else:
        if dp[i+1][j]==-1:
            alpha = uniquePaths2(i+1,j,x,y,dp)
        else:
            alpha = dp[i+1][j]
        if dp[i][j+1]==-1:
            beta = uniquePaths2(i,j+1,x,y,dp)
        else:
            beta = dp[i][j+1]
        return alpha+beta

def uniquePaths3(i,j,x,y):
    return nCr(x+y-2-i-j,y-1-j)

i,j = 0,0
x,y = 2,3
paths = uniquePaths1(i,j,x,y)
print(paths)

dp = []
for _ in range(x+1):
    row = []
    for __ in range(y+1):
        row.append(-1)
    dp.append(row)


paths = uniquePaths2(i,j,x,y,dp)
print(paths)

paths = uniquePaths3(i,j,x,y)
print(paths)