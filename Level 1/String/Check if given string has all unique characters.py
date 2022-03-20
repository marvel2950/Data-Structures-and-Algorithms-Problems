def isAllUnique1(ip_str):
    count = {}
    for i in ip_str:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i]+1
    
    for char,c in count.items():
        if c!=1:
            return False 
    return True


ip_str = 'abcdd'
flag = isAllUnique1(ip_str)
print(flag)

def isAllUnique2(ip_str):
    unique_ip_str = set(ip_str)
    if len(ip_str) == len(unique_ip_str):
        return True
    return False


ip_str = 'abcdd'
flag = isAllUnique2(ip_str)
print(flag)