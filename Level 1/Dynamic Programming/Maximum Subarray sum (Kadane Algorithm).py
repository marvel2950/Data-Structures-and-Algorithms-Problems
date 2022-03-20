import sys
def subArray(arr):
    subList = []
    n = len(arr)
    for i in range(n):
        temp = []
        for j in range(i,n):
            temp.append(arr[j])
            subList.append(temp[::])
            #print(temp,subList)
    return subList

def maxSubArraySum(arr):
    sub = subArray(arr)
    max = -sys.maxsize
    for i in sub:
        # print(sum(i),end=",")
        if sum(i)>max:
            max = sum(i)
    return max 

arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = maxSubArraySum(arr)
print(max_sum)

def maxSubArraySum2(arr):
    n = len(arr)
    max = -sys.maxsize
    for i in range(n):
        temp = 0
        for j in range(i,n):
            temp = temp+arr[j]
            if temp>max:
                max = temp 
    return max

arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = maxSubArraySum2(arr)
print(max_sum)

def maxSubArraySum3(arr):
    n = len(arr)
    max_so_far = -sys.maxsize
    max = 0
    for i in range(n):
        max = max+i 
        if max_so_far<max:
            max_so_far = max 
        if max<0:
            max = 0
        
    return max_so_far

arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = maxSubArraySum2(arr)
print(max_sum)