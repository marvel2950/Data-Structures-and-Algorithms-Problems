def knapsack(weight,value,wt,n):
    if n==0 or wt==0:
        return 0 
    if weight[n-1]<=wt:
        return max( 
                value[n-1]+
                knapsack(weight,value,wt-weight[n-1],n),
                knapsack(weight,value,wt,n-1)
                )
    elif weight[n-1]>wt:
        return knapsack(weight,value,wt,n-1)

weight = [1,3,4,5]
value = [1,4,5,30]
wt = 15
n = len(weight)

val = knapsack(weight,value,wt,n)
print(val)

def knapsack(weight,value,wt,n,dp):
    if n==0 or wt==0:
        return 0 
    if dp[n][wt]!=-1:
        return dp[n][wt]
    if weight[n-1]<=wt:
        dp[n][wt] = max( 
                    value[n-1]+
                    knapsack(weight,value,wt-weight[n-1],n,dp),
                    knapsack(weight,value,wt,n-1,dp)
                    )
        return dp[n][wt]
    elif weight[n-1]>wt:
        dp[n][wt] = knapsack(weight,value,wt,n-1,dp)
        return dp[n][wt]

weight = [1,3,4,5]
value = [1,4,5,30]
wt = 15
n = len(weight)

dp = []
for _ in range(n+1):
    row = []
    for __ in range(wt+1):
        row.append(-1)
    dp.append(row)

val = knapsack(weight,value,wt,n,dp)
#print(dp)
print(val)

def knapsack(weight,value,wt,n):
    dp = []
    for i in range(n+1):
        row = []
        for j in range(wt+1):
            if i==0 or j==0:
                row.append(0)
            else:
                row.append(-1)
        dp.append(row)

    for i in range(n+1):
        for j in range(wt+1):
            if weight[i-1]<=j:
                dp[i][j] = max(
                    value[i-1]+dp[i][j-weight[i-1]],
                    dp[i-1][j]
                )
            elif weight[i-1]>j:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

    
weight = [1,3,4,5]
value = [1,4,5,30]
wt = 15
n = len(weight)

val = knapsack(weight,value,wt,n)
print(val)

