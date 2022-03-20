def solve(start_time,end_time):
    alpha = []
    order = []
    n = len(start_time)
    last_time = -1
    for i in range(n):
        alpha.append([start_time[i],end_time[i]])
    alpha.sort(key=lambda x:x[1])
    for i in range(n):
        if alpha[i][0] > last_time:
            order.append(alpha[i])
            last_time = alpha[i][1]
    return order


start_time = [1,3,0,5,8,5]
end_time = [2,4,6,7,9,9]
order = solve(start_time,end_time)
print(order)