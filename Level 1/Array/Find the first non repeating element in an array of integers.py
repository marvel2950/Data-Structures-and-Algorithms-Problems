def firstNonRepeatingEle(ip_arr):
    count = {}
    for i in ip_arr:
        if i not in count:
            count[i] = 1 
        else:
            count[i] = count[i]+1 
    ans = -1
    for nu,co in count.items():
        if co==1:
            ans = nu
            break
    return ans

ip_arr = [1,1,7,7,5,5,2,9,9]
op_ele = firstNonRepeatingEle(ip_arr)
print(op_ele)