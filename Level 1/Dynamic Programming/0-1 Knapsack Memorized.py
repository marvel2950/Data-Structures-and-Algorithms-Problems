def knapsack(weight,value,wt,n,dp):
    if n==0 or wt==0:
        return 0 
    if dp[n][wt]!=-1:
        return dp[n][wt]
    if weight[n-1]<=wt:
        dp[n][wt] = max( 
                    value[n-1]+
                    knapsack(weight,value,wt-weight[n-1],n-1,dp),
                    knapsack(weight,value,wt,n-1,dp)
                    )
        return dp[n][wt]
    elif weight[n-1]>wt:
        dp[n][wt] = knapsack(weight,value,wt,n-1,dp)
        return dp[n][wt]

weight = [1,3,4,5]
value = [1,4,5,7]
wt = 7
n = len(weight)

dp = []
for _ in range(n+1):
    row = []
    for __ in range(wt+1):
        row.append(-1)
    dp.append(row)

val = knapsack(weight,value,wt,n,dp)
print(dp)
print(val)
