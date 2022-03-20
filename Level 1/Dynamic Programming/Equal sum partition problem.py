def subsetSum(weight,wt,n):
    dp = []
    for i in range(n+1):
        row = []
        for j in range(wt+1):
            if j==0:
                row.append(True)
            elif i==0:
                row.append(False)
            else:
                row.append(-1)
        dp.append(row)

    for i in range(1,n+1):
        for j in range(1,wt+1):
            if weight[i-1]<=j:
                dp[i][j] = dp[i-1][j-weight[i-1]] or dp[i-1][j]
            elif weight[i-1]>j:
                dp[i][j] = dp[i-1][j]

    # for i in dp:
    #     print(*i)
    
    return dp[-1][-1]

def equalSumPart(arr):
    if sum(arr)%2!=0:
        return False 
    wt = sum(arr)//2
    n = len(arr)
    return subsetSum(arr,wt,n)


arr = [2,3,7,8,10,2]
flag = equalSumPart(arr)
print(flag)