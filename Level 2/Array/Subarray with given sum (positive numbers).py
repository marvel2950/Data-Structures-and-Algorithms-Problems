def subArraySum(arr,sum):
    n = len(arr)
    for i in range(n):
        curSum = arr[i]
        for j in range(i+1,len(arr)):
            if sum==curSum:
                ans = str(i)+"->"+str(j-1)
                print(ans)
                return True
            if curSum>sum:
                break
            curSum = curSum+arr[j]
    return False

def subArraySum(arr,sum):
    n = len(arr)
    start = 0
    curSum = arr[0]
    i = 1
    while i<=n:
        while curSum > sum and start < i-1:
            curSum = curSum - arr[start]
            start+=1
        if curSum == sum:
            ans = str(start)+"->"+str(i-1)
            print(ans)
            return True
        if i<n:
            curSum = curSum + arr[i]
        i+=1
    return False

arr = [15,2,4,8,9,5,10,23]
sum = 23
isSumFound =  subArraySum(arr,sum)
print(isSumFound)