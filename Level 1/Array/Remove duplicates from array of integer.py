def removeDup(ip_arr):
    ins = {}
    i = 0
    while i<len(ip_arr):
        if ip_arr[i] in ins:
            ip_arr.pop(i)
        else:
            ins[ip_arr[i]] = 1 
            i=i+1 


ip_arr = [1,7,7,5,2,29]
removeDup(ip_arr)
print(ip_arr)