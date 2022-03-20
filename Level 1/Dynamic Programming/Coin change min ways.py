import sys
def coinChangeMin(coins,sum,n):
    dp = []
    for i in range(n+1):
        row = []
        for j in range(sum+1):
            if j==0:
                row.append(0)
            elif i==0:
                row.append(sys.maxsize)
            else:
                row.append(-1)
        dp.append(row)

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coins[i-1]<=j:
                dp[i][j] = min(
                    1+dp[i][j-coins[i-1]],
                    dp[i-1][j]
                    )
            elif coins[i-1]>j:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

    
coins = [1,2,3]
sum = 5
n = len(coins)

val = coinChangeMin(coins,sum,n)
print(val)

