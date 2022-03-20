def subArraySum(arr,sum):
    n = len(arr)
    for i in range(n):
        curSum = arr[i]
        for j in range(i+1,len(arr)):
            if sum==curSum:
                ans = str(i)+"->"+str(j-1)
                print(ans)
                return True
            curSum = curSum+arr[j]
    return False

def subArraySum(arr,sum):
    n = len(arr)
    map = {}
    curSum = 0
    for i in range(n):
        curSum = curSum+arr[i]
        if sum==curSum:
            ans = str(0)+"->"+str(i)
            print(ans)
            return True
        if curSum-sum in map:
            ans = str(map[curSum-sum]+1)+"->"+str(i)
            print(ans)
            return True
        map[curSum] = i   
    return False

arr = [10,2,-2,-20,10]
sum = -10
isSumFound =  subArraySum(arr,sum)
print(isSumFound)