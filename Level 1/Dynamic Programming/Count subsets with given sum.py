def subsetsWithGivenSum(weight,wt,n):
    dp = []
    for i in range(n+1):
        row = []
        for j in range(wt+1):
            if j==0:
                row.append(1)
            elif i==0:
                row.append(0)
            else:
                row.append(-1)
        dp.append(row)

    for i in range(1,n+1):
        for j in range(1,wt+1):
            if weight[i-1]<=j:
                dp[i][j] = dp[i-1][j-weight[i-1]] + dp[i-1][j]
            elif weight[i-1]>j:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

arr = [2,3,5,6,8,10]
sum = 100
n = len(arr)

count = subsetsWithGivenSum(arr,sum,n)
print(count)


