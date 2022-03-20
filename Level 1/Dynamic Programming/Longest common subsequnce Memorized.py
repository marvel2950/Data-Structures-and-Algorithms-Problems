def lcs(x,y,n,m,dp):
    if n==0 or m==0:
        return 0
    if dp[n][m]!=-1:
        return dp[n][m]
    if x[n-1] == y[m-1]:
        dp[n][m] = 1+ lcs(x,y,n-1,m-1,dp)
        return dp[n][m]
    else:
        dp[n][m] = max(lcs(x,y,n-1,m,dp),lcs(x,y,n,m-1,dp))
        return dp[n][m]

x = "abcde"
y = "ace"
n = len(x)
m = len(y)

dp = []
for _ in range(n+1):
    row = []
    for __ in range(m+1):
        row.append(-1)
    dp.append(row)

length = lcs(x,y,n,m,dp)
print(length)