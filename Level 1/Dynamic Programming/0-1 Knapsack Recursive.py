def knapsack(weight,value,wt,n):
    if n==0 or wt==0:
        return 0 
    if weight[n-1]<=wt:
        return max( 
                value[n-1]+
                knapsack(weight,value,wt-weight[n-1],n-1),
                knapsack(weight,value,wt,n-1)
                )
    elif weight[n-1]>wt:
        return knapsack(weight,value,wt,n-1)

weight = [1,3,4,5]
value = [1,4,5,7]
wt = 7
n = len(weight)

val = knapsack(weight,value,wt,n)
print(val)
