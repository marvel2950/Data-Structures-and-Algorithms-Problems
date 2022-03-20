def firstRepeatingEle(ip_arr):
    count = {}
    ans = -1
    for i in ip_arr:
        if i not in count:
            count[i] = 1 
        else:
            ans = i 
            break
    return ans

ip_arr = [1,7,7,1,5,2,2,9]
op_ele = firstRepeatingEle(ip_arr)
print(op_ele)