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
                    value[i-1]+dp[i-1][j-weight[i-1]],
                    dp[i-1][j]
                )
            elif weight[i-1]>j:
                dp[i][j] = dp[i-1][j]

    for i in dp:
        print(*i)

    return dp[-1][-1]

    
weight = [1,3,4,5]
value = [1,4,5,7]
wt = 7
n = len(weight)

val = knapsack(weight,value,wt,n)
print(val)
