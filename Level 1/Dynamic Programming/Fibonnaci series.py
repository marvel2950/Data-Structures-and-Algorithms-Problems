# def fibonnaci(n):
#     if n==1:
#         return 0 
#     elif n==2:
#         return 1
#     return fibonnaci(n-1)+fibonnaci(n-2)

# def fibonnaci(n,dp):
#     if dp[n]!=-1:
#         return dp[n]
#     if n==1:
#         dp[n] = 0
#         return dp[n]
#     elif n==2:
#         dp[n] = 1
#         return dp[n]
#     dp[n] = fibonnaci(n-1,dp)+fibonnaci(n-2,dp)
#     return dp[n]

def fibonnaci(n):
    arr = [0,1]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n-1]

n = 6
# dp = []
# for _ in range(n+1):
#     dp.append(-1)
fib = fibonnaci(n)
# print(dp)
print(fib)