def reverse1(ip_arr):
    op_arr = [-1]*len(ip_arr) #[-1,-1,-1,-1,-1]
    j = 0 
    for i in range(len(ip_arr)-1,-1,-1):
        op_arr[j] = ip_arr[i]
        j=j+1 
    return op_arr

ip_arr = [1,2,3,4,5]
op_arr = reverse1(ip_arr)
print(op_arr)

def reverse2(ip_arr):
    i = 0
    j = len(ip_arr)-1
    while i<j:
        ip_arr[i],ip_arr[j] = ip_arr[j],ip_arr[i]
        i+=1 
        j-=1 
    return ip_arr

ip_arr = [1,2,3,4,5]
op_arr = reverse2(ip_arr)
print(op_arr)