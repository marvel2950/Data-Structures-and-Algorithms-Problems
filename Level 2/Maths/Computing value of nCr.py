#Brute
def fact(n):
    res = 1 
    for i in range(2,n+1):
        res=res*i 
    return res

def nCr(n,r):
    return fact(n)//(fact(r)*fact(n-r))

n = 5
r = 2
print(nCr(n,r))

#Recursive
def nCr(n,r):
    if r>n:
        return 0
    elif r==0 or r==n:
        return 1
    return nCr(n-1,r-1)+nCr(n-1,r)

n = 5
r = 2
print(nCr(n,r))

#Memorised
def nCrUtil(n,r,dp):
    if dp[n][r]!=-1:
        return dp[n][r]
    if r==0 or r==n:
        dp[n][r] = 1
        return dp[n][r]
    dp[n][r] =  nCr(n-1,r-1)+nCr(n-1,r)
    return dp[n][r]

def nCr(n,k):
    dp = [[-1 for y in range(k+1)]
            for x in range(n+1)]
    return nCrUtil(n,k,dp)
    
n = 5
r = 2
print(nCr(n,r))

def nCr(n,k):
    dp = [[-1 for y in range(k+1)]
            for x in range(n+1)]

    for i in range(0,n+1):
        for j in range(0,k+1):
            if j==0 or j==i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    return dp[-1][-1]
    
n = 5
r = 2
print(nCr(n,r))