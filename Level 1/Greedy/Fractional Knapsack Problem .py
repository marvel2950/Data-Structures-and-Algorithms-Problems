def knapsack(wt,values,weight):
    n = len(values)
    items = []
    for i in range(n):
        items.append([values[i]/weight[i],i])
    items.sort(key=lambda j:j[0],reverse=True)
    print(items)
    profit = 0
    for i in range(n):
        if wt>0:
            idx = items[i][1] 
            if wt >= weight[idx]:
                profit += values[idx]
                wt -= weight[idx]
            else:
                profit += items[i][0]*wt 
                wt = 0
        else:
            break 
    return profit

wt = 50 
values = [60,100,120]
weight = [10,20,30]
profit = knapsack(wt,values,weight)
print(profit)