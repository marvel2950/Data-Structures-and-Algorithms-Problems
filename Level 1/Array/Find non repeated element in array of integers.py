def nonRepeatingEle(ip_arr):
    count = {}
    for i in ip_arr:
        if i not in count:
            count[i] = 1 
        else:
            count[i] = count[i]+1 
    ans = []
    for nu,co in count.items():
        if co==1:
            ans.append(nu)
    return ans 

ip_arr = [1,7,7,5,2,2,9]
op_arr = nonRepeatingEle(ip_arr)
print(op_arr)