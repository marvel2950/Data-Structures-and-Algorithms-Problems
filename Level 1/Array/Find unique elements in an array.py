def uniqueEle1(ip_arr):
    ins = {}
    for i in ip_arr:
        ins[i] = True
    # ans = []
    # for key,value in ins.items():
    #     ans.append(key)
    ans = list(ins.keys())
    return ans

ip_arr = [1,7,7,5,2,2,9]
op_arr = uniqueEle1(ip_arr)
print(op_arr)

def uniqueEle2(ip_arr):
    ans = list(set(ip_arr))
    return ans

ip_arr = [1,7,7,5,2,2,9]
op_arr = uniqueEle2(ip_arr)
print(op_arr)